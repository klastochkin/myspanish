"""JWT authentication + file-based password store + session tracking."""

import hashlib
import json
import os
import threading
from datetime import datetime, timezone
from pathlib import Path

import jwt

from users import USERS

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
PASSWORDS_FILE = Path("passwords.json")
SESSIONS_FILE = Path("sessions.json")

_lock = threading.Lock()


def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# ── Password store (passwords.json) ──────────────────────────────────────────

def _load_passwords() -> dict:
    if PASSWORDS_FILE.exists():
        with PASSWORDS_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_passwords(data: dict) -> None:
    with PASSWORDS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def has_password(name: str) -> bool:
    """Return True if this user already set a password."""
    with _lock:
        return name in _load_passwords()


def set_password(name: str, password: str) -> None:
    """Store a hashed password for *name*."""
    with _lock:
        data = _load_passwords()
        data[name] = _hash(password)
        _save_passwords(data)


def clear_password(name: str) -> None:
    """Remove the password for *name* (forces re-set on next login)."""
    with _lock:
        data = _load_passwords()
        data.pop(name, None)
        _save_passwords(data)


def verify_user(name: str, password: str) -> dict | None:
    """Return user dict if credentials are valid, else None."""
    user = USERS.get(name)
    if not user:
        return None
    with _lock:
        stored_hash = _load_passwords().get(name)
    if not stored_hash:
        return None
    if stored_hash != _hash(password):
        return None
    return {"name": name, **user}


# ── JWT helpers ──────────────────────────────────────────────────────────────

def create_token(name: str, role: str, days: int) -> str:
    exp = datetime.now(timezone.utc).timestamp() + days * 86400
    return jwt.encode({"sub": name, "role": role, "exp": exp},
                      SECRET_KEY, algorithm="HS256")


def decode_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return None


# ── Session file I/O (thread-safe) ───────────────────────────────────────────

def _load_sessions() -> list:
    if SESSIONS_FILE.exists():
        with SESSIONS_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_sessions(sessions: list) -> None:
    with SESSIONS_FILE.open("w", encoding="utf-8") as f:
        json.dump(sessions, f, ensure_ascii=False, indent=2)


def record_event(user: str, event_type: str, detail: dict | None = None) -> None:
    """Append an event to the current session for *user*."""
    with _lock:
        sessions = _load_sessions()

        current = None
        for s in reversed(sessions):
            if s["user"] == user:
                current = s
                break

        if event_type == "login" or current is None:
            current = {
                "user": user,
                "started": datetime.now(timezone.utc).isoformat(),
                "events": [],
            }
            sessions.append(current)

        event = {"type": event_type, "ts": datetime.now(timezone.utc).isoformat()}
        if detail:
            event.update(detail)
        current["events"].append(event)

        _save_sessions(sessions)


def get_sessions() -> list:
    with _lock:
        return _load_sessions()


def delete_sessions() -> int:
    with _lock:
        sessions = _load_sessions()
        count = len(sessions)
        _save_sessions([])
        return count
