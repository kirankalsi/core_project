#! /bin/bash

ssh kiran11kalsi@34.105.145.24 << EOF

cd core_project
git pull
. .env
env DB_URI=${DB_URI} env SECRET_KEY=${SECRET_KEY} env MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} docker stack deploy --compose-file docker-compose.yaml core_project_stack

EOF