# Learn Docker

Learn containers with me by doing. I am currently exploring containers and documenting the journey with this demo project. The aim is to understand how to setup a multi-container application with the following services:

  - Node.js Web App (Express.js)
  - PostgreSQL Database
  - Redis Caching Service

The containers would be built from scratch with Docker Compose and other features would be added for complexity. It may not be an impressive app but it affords the opportunity to learn. Let's get started! The app is written in NodeJS (ExpressJS) and it is to display inspirational quotes. In the future I plan to integrate GenAI is possible. You may wish to clone this repo and follow along. I would try to explain some of the challenges and how I overcame it.


Build the entire Application stack by running: 
`docker compose up -d`

To rebuild the containers after making changes, run:
`docker compose up -d --build`

The `-d` flag runs your application in a detached mode so you can still have access to the teminal. This runs all services in the background.

To check the running containers
`docker ps`

Stop the Application

`docker compose down`

View Logs for the App

`docker compose logs -f app`

Access PostgreSQL Database

`docker exec -it postgres_db psql -U user -d mydatabase`

Test Redis Connection

`docker exec -it redis_cache redis-cli`

List Networks

`docker network ls`

Inspect Network Details

`docker network inspect app_network`

