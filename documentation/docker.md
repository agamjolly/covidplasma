# Useful Docker Commands

Making a Docker image using the Dockerfile.

`docker build -t covidplasma .`

Running the Docker image on port 80. 

`docker run -p 80:80 covidplasma`

Stopping all Docker containers.

`docker stop $(docker ps -aq)`

Deleting all Docker containers.

`docker rm $(docker ps -aq)`

Running the Docker image until stopped.

`docker run -d --restart unless-stopped -p 80:80 covidplasma`
