# Docker App — CCS3308 Assignment 1

## Deployment Requirements
- Docker Engine 24.x
- Docker Compose v2.x
- Git

## Application Description
A web-based visit counter application with two Docker services.
Flask web server counts and displays total visits stored in MySQL database.

## Network and Volume Details
| Resource | Name | Purpose |
|---|---|---|
| Network | app-net | Communication between containers |
| Volume | mysql-data | Persists database data |

## Container Configuration
### flask-web
- Image: custom build
- Port: 5000
- Restart: unless-stopped

### mysql-db
- Image: mysql:8.0
- Port: 3306
- Restart: unless-stopped

## Container List
| Container | Role |
|---|---|
| flask-web | Serves web application on port 5000 |
| mysql-db | Stores visit count data |

## Instructions
### Prepare
./prepare-app.sh

### Start
./start-app.sh

### Access
Open browser: http://localhost:5000

### Stop
./stop-app.sh

### Remove
./remove-app.sh

## Example Workflow
./prepare-app.sh
Preparing app ...
./start-app.sh
Running app ...
The app is available at http://localhost:5000
./stop-app.sh
Stopping app ...
./remove-app.sh
Removed app.

## References
- Docker Docs: https://docs.docker.com
- Flask Docs: https://flask.palletsprojects.com
- MySQL Hub: https://hub.docker.com/_/mysql
