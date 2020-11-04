# Assignment
`Using tooling of your choice, provide code/documentation for deploying a load-balanced web server into Minikube, including a way to prove the requests are load-balanced.`


# Plan
 - [x] flask webapp using web service (frontend)
 - [x] microservice to return color from env var (backend)
 - [x] Dockerize nginx webserver + microservice ( dockercompose + javascript)
 - [x] Kubernetes chart for Deployment + Service
 - [ ] Hashicorp Waypoint for Build & Deploy
 - [ ] Load testing container
 - [ ] Logs files monitoring 
 - [ ] istio service mesh
 - [ ] isto dashboard demo URLs etc.
 

# Implementation Log

### flask webapp using web service
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

### Microservice
 * feature branch
 * reorg code for frontend & backend
 * copy/ pasta fronend to backend
 * change port
 * change template to a versioned API json file
 * change reponse mimetype 
 * Add env variables (with defaults)
 * test by hand
 * Add usages to README.md


### Dockerize nginx webserver + microservice
 * reorg paths, remove unwanted nesting
 * add docker-compose file
 * write javascript for frontend
 * Deal with CORS for API
 

```shell script
cd demoapp
docker-compose up
docker-compose down --volumes

```

```shell script
curl http://localhost:58080/
curl http://localhost:58081/api/v1/colour.json
curl http://localhost:58082/api/v1/colour.json

```


Hot restart
```shell script
touch frontend/uwsgi.ini
# and/or 
touch backend/uwsgi.ini

```

### Kubernetes chart for Deployment + Service
For docker-windows kubernetes
```shell script
export KUBECONFIG=/c/Users/gregn/.kube/config
kubectl config get-contexts

```
 * `kompose` to convert docker-compose.yaml to k8s definitions
 * de-hardcode backend URL in frontend
 * rewrite `kompose` stuff by hand. Going with `NodePort` services for now

```shell script
cd kubernetes
kubectl apply -f .
kubectl get nodes
kubectl get svc  # <-------- get localhost ports from here

```
these'll be busted if the port moves
[backend URL](http://localhost:30039/)
[frontend URL](http://localhost:30467/api/v1/colour.json)

### Hashicorp Waypoint for Build & Deploy
 
[Hashicorp Waypoint](https://www.waypointproject.io/docs/getting-started)

 ```shell script
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install waypoint

```

```shell script
docker pull hashicorp/waypoint:latest
waypoint install -platform=docker -accept-tos

```

