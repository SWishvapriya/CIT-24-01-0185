#!/bin/bash

echo "Preparing application..."

docker volume create mysql-data

docker compose build

echo "Preparation completed."
