#!/bin/bash
source .venv/bin/activate
cd src
pip install --upgrade pip
pip install -r requirements.txt
python3 setup.py build