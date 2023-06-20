#!/usr/bin/env bash

cd ~/git/Pegelwacht/src || exit 1

source venv/bin/activate || exit 1

python3 import_data.py -c ../pegelwacht.cfg || exit 1

exit 0