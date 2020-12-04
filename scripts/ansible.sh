#!/bin/bash

mkdir -p ~/.local/bin
echo 'PATH=$PATH:home/jenkins/.local/bin' >> ~/.bashrc
source ~/.bashrc

git clone https://github.com/kirankalsi/core_project.git
cd core_project
git checkout ansible
ansible-playbook -i inventory playbook.yaml