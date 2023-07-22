#!/bin/bash

cd ~/portfolio
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
sudo systemctl daemon-reload
sudo systemctl restart myportfolio
