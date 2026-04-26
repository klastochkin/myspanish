import os

from fastapi import Cookie, FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from auth import (
    clear_password,
    create_token,
    decode_token,
    delete_sessions,
    get_sessions,
    has_password,
    record_event,
    set_password,
    verify_user,
)
from data import LESSONS
from users import USERS

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Optional env-var for emergency password resets (see /reset-password endpoint)
RESET_KEY = os.environ.get("RESET_KEY", "")


# ── Auth helpers ──────────────────────────────────────────────────────────────

def _get_user(token: str | None) -> dict | None:
    """Decode JWT and return {"name": ..., "role": ...} or None."""
    if not token:
        return None
    payload = decode_token(token)
    if not payload:
        return None
    return {"name": payload["sub"], "role": payload["role"]}


# ── Login / Logout / Set-password ─────────────────────────────────────────────

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request, error: str = "", msg: str = ""):
    return templates.TemplateResponse(request, "login.html",
                                      {"error": error, "msg": msg})


@app.post("/login")
def login(name: str = Form(...), password: str = Form(...)):
    # Unknown user?
    if name not in USERS:
        return RedirectResponse("/login?error=Invalid+name+or+password",
                                status_code=303)

    # No password yet → redirect to set-password page
    if not has_password(name):
        response = RedirectResponse("/set-password", status_code=303)
        # Stash the name in a short-lived cookie so the set-password page knows who
        response.set_cookie("setup_user", name, max_age=300,
                            httponly=True, samesite="lax")
        return response

    # Normal verification
    user_info = verify_user(name, password)
    if not user_info:
        return RedirectResponse("/login?error=Invalid+name+or+password",
                                status_code=303)

    return _issue_login(name, user_info["role"])


@app.get("/set-password", response_class=HTMLResponse)
def set_password_page(request: Request, error: str = "",
                      setup_user: str | None = Cookie(default=None)):
    if not setup_user or setup_user not in USERS:
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse(request, "set_password.html",
                                      {"name": setup_user, "error": error})


@app.post("/set-password")
def do_set_password(password: str = Form(...), confirm: str = Form(...),
                    setup_user: str | None = Cookie(default=None)):
    if not setup_user or setup_user not in USERS:
        return RedirectResponse("/login", status_code=303)

    if len(password) < 3:
        return RedirectResponse("/set-password?error=Password+must+be+at+least+3+characters",
                                status_code=303)
    if password != confirm:
        return RedirectResponse("/set-password?error=Passwords+do+not+match",
                                status_code=303)

    set_password(setup_user, password)
    role = USERS[setup_user]["role"]
    response = _issue_login(setup_user, role)
    response.delete_cookie("setup_user")
    return response


def _issue_login(name: str, role: str) -> RedirectResponse:
    """Create JWT, set cookie, record login event, redirect."""
    days = 7 if role == "user" else 1
    token = create_token(name, role, days)
    dest = "/supervisor" if role == "supervisor" else "/"
    response = RedirectResponse(dest, status_code=303)
    response.set_cookie("token", token, max_age=days * 86400,
                        httponly=True, samesite="lax")
    record_event(name, "login")
    return response


@app.get("/logout")
def logout():
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("token")
    return response


# ── Emergency reset via env-var key ──────────────────────────────────────────

@app.get("/reset-password")
def reset_password_via_key(key: str = "", user: str = ""):
    """GET /reset-password?key=RESET_KEY&user=F  — clears password for user."""
    if not RESET_KEY or key != RESET_KEY:
        raise HTTPException(403, "Forbidden. Set RESET_KEY env var and pass ?key=...")
    if user not in USERS:
        raise HTTPException(404, f"Unknown user: {user}")
    clear_password(user)
    return RedirectResponse(
        f"/login?msg=Password+for+{user}+has+been+reset.+Log+in+to+set+a+new+one.",
        status_code=303)


# ── Pages ─────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def index(request: Request, token: str | None = Cookie(default=None)):
    user = _get_user(token)
    if not user:
        return RedirectResponse("/login", status_code=303)
    vocab_lessons = LESSONS.get("vocabulary", {})
    total_words = sum(len(v.get("words", {})) for v in vocab_lessons.values())
    return templates.TemplateResponse(request, "index.html", {
        "user": user,
        "total_words": total_words,
    })


@app.get("/vocabulary", response_class=HTMLResponse)
def vocabulary(request: Request, token: str | None = Cookie(default=None)):
    user = _get_user(token)
    if not user:
        return RedirectResponse("/login", status_code=303)
    lessons = [
        {"id": k, "title": v["title"], "subtitle": v["subtitle"],
         "count": len(v["words"])}
        for k, v in LESSONS["vocabulary"].items()
    ]
    return templates.TemplateResponse(request, "vocab.html",
                                      {"lessons": lessons, "user": user})


# ── Supervisor ────────────────────────────────────────────────────────────────

@app.get("/supervisor", response_class=HTMLResponse)
def supervisor_page(request: Request, token: str | None = Cookie(default=None)):
    user = _get_user(token)
    if not user or user["role"] != "supervisor":
        return RedirectResponse("/login", status_code=303)
    sessions = get_sessions()
    user_list = [{"name": n, "role": u["role"], "has_pw": has_password(n)}
                 for n, u in USERS.items()]
    return templates.TemplateResponse(request, "supervisor.html",
                                      {"user": user, "sessions": sessions,
                                       "user_list": user_list})


@app.get("/api/sessions/download")
def download_sessions(token: str | None = Cookie(default=None)):
    user = _get_user(token)
    if not user or user["role"] != "supervisor":
        raise HTTPException(403)
    return JSONResponse(
        content=get_sessions(),
        headers={"Content-Disposition": "attachment; filename=sessions.json"},
    )


@app.post("/api/sessions/delete")
def delete_all_sessions(token: str | None = Cookie(default=None)):
    user = _get_user(token)
    if not user or user["role"] != "supervisor":
        raise HTTPException(403)
    count = delete_sessions()
    return {"deleted": count}


@app.post("/api/reset-password/{target_user}")
def reset_user_password(target_user: str,
                        token: str | None = Cookie(default=None)):
    """Supervisor resets a user's password (forces re-set on next login)."""
    user = _get_user(token)
    if not user or user["role"] != "supervisor":
        raise HTTPException(403)
    if target_user not in USERS:
        raise HTTPException(404)
    clear_password(target_user)
    return {"ok": True, "user": target_user}


# ── Quiz API ──────────────────────────────────────────────────────────────────

@app.get("/api/vocabulary/{lesson_id}")
def api_vocab(lesson_id: str, token: str | None = Cookie(default=None)):
    if not _get_user(token):
        raise HTTPException(403)
    lesson = LESSONS["vocabulary"].get(lesson_id)
    if not lesson:
        raise HTTPException(404)
    return {"title": lesson["title"], "subtitle": lesson["subtitle"],
            "words": lesson["words"]}


# ── Event recording API ──────────────────────────────────────────────────────

@app.post("/api/event")
async def record_quiz_event(request: Request,
                            token: str | None = Cookie(default=None)):
    user = _get_user(token)
    if not user:
        raise HTTPException(403)
    body = await request.json()
    event_type = body.get("type")
    if event_type not in ("good_answer", "bad_answer"):
        raise HTTPException(400, "Invalid event type")
    detail = {k: v for k, v in body.items() if k != "type"}
    record_event(user["name"], event_type, detail)
    return {"ok": True}
