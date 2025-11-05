#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate
export FLASK_APP=run.py
python run.py
