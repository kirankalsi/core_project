#!/bin/bash

cd core_project
git pull
git checkout ansible
echo ${PATH}
ansible-playbook -i inventory playbook.yaml