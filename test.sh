#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

echo "ruff check"
ruff check .

echo "ruff format --diff ."
ruff format --diff .

uv run py.test