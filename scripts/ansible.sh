#!/bin/bash

sudo apt install python3-pip
mkdir -p ~/.local/bin
echo 'PATH=$PATH:home/jenkins/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install --user ansible

git clone https://github.com/kirankalsi/core_project.git
cd core_project
git checkout ansible
ansible-playbook -i inventory playbook.yaml