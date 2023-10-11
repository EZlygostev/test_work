#!/bin/bash
pip install --upgrade pip
cd app
pip install -r requirements.txt
python3 create_table.py
uvicorn main:app --host 0.0.0.0 --port 80