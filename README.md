# Assignment
`Using tooling of your choice, provide code/documentation for deploying a load-balanced web server into Minikube, including a way to prove the requests are load-balanced.`


# Plan
 * microservice to return color from env var
 * flask webapp using web service
 * Dockerize nginx webserver + microservice
 * Kubernetes chart for Deployment + Service
 * Load testing container
 * Logs files monitoring 
 * istio service mesh
 * isto dashboard demo URLs etc.
 

# Implementation

 ## color microservice
 * Using alpine linux for image size & reduced attack surface
 * rip & copy pasta [tutorial](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04) for starting point
 * Review upstream dockerfiles
 * Changes to bash script
 * first bug "nginx bad gateway" 
   - `exec` into container and check logs 
        - nginx logs redirected to stdout & stderr
        - start.sh volume path was incorrect
   - add `touch-reload = /app/uwsgi.ini` feature