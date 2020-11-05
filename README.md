# Assignment
`Using tooling of your choice, provide code/documentation for deploying a load-balanced web server into Minikube, including a way to prove the requests are load-balanced.`


# Plan
 - [x] flask webapp using web service (frontend)
 - [x] microservice to return color from env var (backend)
 - [x] Dockerize nginx webserver + microservice ( dockercompose + javascript)
 - [x] Kubernetes chart for Deployment + Service
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
 * copy/pasta frontend to backend
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
kubectl get pods
kubectl get svc  # <-------- get localhost ports from here

kubectl get pods
kubectl exec -it backend-deployment-6d87dd5c9b-m95z6 frontend -- bash

kubectl logs -f -l app=frontend -c frontend

```
these'll be busted if the port moves
[backend URL](http://localhost:30039/)
[frontend URL](http://localhost:30467/api/v1/colour.json)

Verifying load balancing
```shell script
kubectl describe svc backend  # check endpoints

#seperate terminals
kubectl logs -f frontend-deployment-697fd67fc5-4lc78 -c frontend
kubectl logs -f frontend-deployment-697fd67fc5-894dq -c frontend
kubectl logs -f frontend-deployment-697fd67fc5-b7fzh -c frontend
```

Cleanup
```shell script
kubectl delete deployment backend-deployment-v1
kubectl delete deployment backend-deployment-v2
kubectl delete deployment frontend-deployment

kubectl delete service backend
kubectl delete service frontend

```


### Istio Service Mesh


Install Istio somewhere
```shell script
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.7.4
export PATH=$PWD/bin:$PATH

```
Istio demo profile
```shell script
cd istio-1.7.4
istioctl install --set profile=demo
kubectl label namespace default istio-injection=enabled
```

Ingress Gateway
```shell script
kubectl apply -f istio/gateway.yaml

kubectl get svc istio-ingressgateway -n istio-system

```

```shell script
kubectl apply -f istio/backend-virtualservice.yaml
kubectl apply -f istio/frontend-virtualservice.yaml

```

Redeploy the workload
```shell script

```

Manual Test
 - [http://frontend.localhost/]()
