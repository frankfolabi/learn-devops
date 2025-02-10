# Learn Containers with me

I am currently exploring containers and would like to share this demo project. The aim is to understand how to setup a multi-container application with the following services:

  - Node.js Web App (Express.js)
  - PostgreSQL Database
  - Redis Caching Service

The containers would be built from scratch with Docker Compose and other features would be added for complexity. Let's start!

Clone this repo and cd in to the app folder. You may wish to inspect the files.

Start the Application by running: 
`docker compose up -d`


To rebuild the containers

docker compose up -d --build
This runs all services in the background.

Check Running Containers

docker ps

Stop the Application

docker compose down

View Logs for the App

docker compose logs -f app

Access PostgreSQL Database

docker exec -it postgres_db psql -U user -d mydatabase

Test Redis Connection

docker exec -it redis_cache redis-cli

List Networks

docker network ls

Inspect Network Details

docker network inspect app_network

