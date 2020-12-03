#! /bin/bash

sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv proj_venv
. proj_venv/bin/activate
pip3 install -r app1/requirements.txt app2/requirements.txt app3/requirements.txt app4/requirements.txt

pytest ./app1 --cov ./app1/application
pytest ./app2 --cov ./app2/application
pytest ./app3 --cov ./app3/application
pytest ./app4 --cov ./app4/application

deactivate
rm -rf proj_venv