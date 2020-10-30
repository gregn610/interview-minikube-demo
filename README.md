# Assignment
`Using tooling of your choice, provide code/documentation for deploying a load-balanced web server into Minikube, including a way to prove the requests are load-balanced.`


# Plan
 * flask webapp using web service (frontend)
 * microservice to return color from env var (backend)
 * Dockerize nginx webserver + microservice
 * Kubernetes chart for Deployment + Service
 * Load testing container
 * Logs files monitoring 
 * istio service mesh
 * isto dashboard demo URLs etc.
 

# Implementation

## flask webapp using web service
 * Using alpine linux for image size & reduced attack surface
 * rip & copy pasta [tutorial](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04) for starting point
 * Review upstream dockerfiles
 * Changes to bash script
 * first bug "nginx bad gateway" 
   - `exec` into container and check logs 
        - nginx logs redirected to stdout & stderr
        - start.sh volume path was incorrect
   - add `touch-reload = /app/uwsgi.ini` feature
   - test by hand
   - git initial commit

## Microservice
 * feature branch
 * reorg code for frontend & backend
 * copy/ pasta fronend to backend
 * change port
 * change template to a versioned API json file
 * change reponse mimetype 
 * Add env variables (with defaults)
 * test by hand
 * Add usages to README.md
  
### Usage
use provided `./start.sh` or
 
```shell script
cd src/backend/var/www/TestApp

docker run -d -p 58081:80 --name=demo.backend -v $PWD:/app -e DEMO_FOREGROUND_COLOUR=green demo.backend

docker kill demo.backend
docker rm demo.backend

```

## Dockerize nginx webserver + microservice

```shell script
cd src
docker-compose up

docker-compose down --volumes

```
