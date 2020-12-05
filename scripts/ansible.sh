#!/bin/bash

cd core_project
git pull
git checkout ansible
ansible-playbook -i inventory playbook.yaml