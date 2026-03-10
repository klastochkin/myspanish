#!/usr/bin/env bash

set -euo pipefail

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8000}"

echo "Starting local server on http://${HOST}:${PORT}"
exec python3 -m uvicorn main:app --reload --host "${HOST}" --port "${PORT}"
