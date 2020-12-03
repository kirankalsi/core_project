#! /bin/bash

ssh kiran11kalsi@34.105.145.24 << EOF

docker pull kiran11kalsi/app1:latest
docker pull kiran11kalsi/app2:latest
docker pull kiran11kalsi/app3:latest
docker pull kiran11kalsi/app4:latest
cd core_project
git pull
docker stack deploy --compose-file docker-compose.yaml core_project_stack

EOF