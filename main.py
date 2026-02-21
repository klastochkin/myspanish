import hashlib
import hmac
import os

from fastapi import Cookie, FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from data import LESSONS, PRONOUNS, TENSE_NAMES

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# If PRIVATE_KEY is not set, auth is disabled (safe for local dev).
PRIVATE_KEY = os.environ.get("PRIVATE_KEY", "")


def _token() -> str:
    return hmac.new(PRIVATE_KEY.encode(), b"spanish-quiz", hashlib.sha256).hexdigest()


def _authed(access: str | None) -> bool:
    if not PRIVATE_KEY:
        return True
    return bool(access) and hmac.compare_digest(access, _token())


def _guard(access: str | None) -> None:
    if not _authed(access):
        raise HTTPException(status_code=403, detail="Access denied. Visit /unlock?key=YOUR_KEY")


# ── Auth ──────────────────────────────────────────────────────────────────────

@app.get("/unlock")
def unlock(key: str, response: Response):
    if not PRIVATE_KEY or key != PRIVATE_KEY:
        raise HTTPException(403, "Wrong key.")
    response.set_cookie("access", _token(), max_age=60 * 60 * 24 * 365,
                        httponly=True, samesite="lax")
    return RedirectResponse("/")


# ── Pages ─────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def index(request: Request, access: str | None = Cookie(default=None)):
    _guard(access)
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/vocabulary", response_class=HTMLResponse)
def vocabulary(request: Request, access: str | None = Cookie(default=None)):
    _guard(access)
    lessons = [
        {"id": k, "title": v["title"], "subtitle": v["subtitle"],
         "count": len(v["words"])}
        for k, v in LESSONS["vocabulary"].items()
    ]
    return templates.TemplateResponse("vocab.html", {"request": request, "lessons": lessons})


@app.get("/conjugation", response_class=HTMLResponse)
def conjugation(request: Request, access: str | None = Cookie(default=None)):
    _guard(access)
    lessons = [
        {"id": k, "title": v["title"], "subtitle": v["subtitle"],
         "count": len(v["verbs"])}
        for k, v in LESSONS["conjugation"].items()
    ]
    return templates.TemplateResponse("conj.html", {"request": request, "lessons": lessons})


# ── API ───────────────────────────────────────────────────────────────────────

@app.get("/api/vocabulary/{lesson_id}")
def api_vocab(lesson_id: str, access: str | None = Cookie(default=None)):
    _guard(access)
    lesson = LESSONS["vocabulary"].get(lesson_id)
    if not lesson:
        raise HTTPException(404)
    return {"title": lesson["title"], "subtitle": lesson["subtitle"],
            "words": lesson["words"]}


@app.get("/api/conjugation/{lesson_id}")
def api_conj(lesson_id: str, access: str | None = Cookie(default=None)):
    _guard(access)
    lesson = LESSONS["conjugation"].get(lesson_id)
    if not lesson:
        raise HTTPException(404)
    return {"title": lesson["title"], "subtitle": lesson["subtitle"],
            "verbs": lesson["verbs"], "tense_names": TENSE_NAMES,
            "pronouns": PRONOUNS}
