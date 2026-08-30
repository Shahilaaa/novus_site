#!/bin/bash
set -e
pip install --break-system-packages -r requirements.txt
python3 manage.py collectstatic --noinput --clear
