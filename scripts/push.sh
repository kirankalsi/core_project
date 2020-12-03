#! /bin/bash

docker-compose push
env DB_URI=${DB_URI} env MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}