#!/bin/bash
if [! -d "venv" ]; then
    python3 -m venv venv/
    echo "No venv/ folder found, creating venv"
else
    echo "venv/ folder found"
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r src/requirements.txt
python3 setup.py build
./build/exe.macosx-15.0-arm64-3.13/despair