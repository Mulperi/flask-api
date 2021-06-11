# Local development database in a Docker container

- Build image from the Dockerfile inside this directory: `docker build -t psqlimage .`.
- Run the new container: `docker run --name mypostgrescontainer -p 5555:5432 psqlimage`. Notice that your (host) port 5555 will be forwarded to containers port 5432 where the postgresql is listening.
- The PostgreSQL database in the container will be initialized and populated with `init.sql`.









