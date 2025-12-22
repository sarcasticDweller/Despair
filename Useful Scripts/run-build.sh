#!/usr/bin/env bash
# add me to path: `export PATH=$PATH:Useful\ Scripts/run-build.sh`
source venv/bin/activate
pip install -r src/requirements.txt
python3 setup.py build
./build/exe.macosx-15.0-arm64-3.13/despair