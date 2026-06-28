#!/bin/bash

echo "Removing application..."

docker compose down

docker volume rm mysql-data

echo "Removed app."
