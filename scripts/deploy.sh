#! /bin/bash

ssh kiran11kalsi@34.105.145.24 << EOF

cd core_project
git pull
docker stack deploy --compose-file docker-compose.yaml core_project_stack

EOF