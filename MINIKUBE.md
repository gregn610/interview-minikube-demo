```powershell
minikube config set memory 5120
minikube start --extra-config=apiserver.service-node-port-range=1-65535
# minikube docker-env
& minikube -p minikube docker-env | Invoke-Expression

```

# Docker build images
```powershell
cd backend
docker build --no-cache . -t demoapp_backend:v1
docker build --no-cache . -t demoapp_backend:v2

cd ..\frontend
docker build --no-cache . -t demoapp_frontend:v1
docker build --no-cache . -t demoapp_frontend:v2

cd ..
docker images

```

# Using docker-compose to build the images
### v1
```powershell
cd C:\Users\gregn\Dev\minikube\demoapp
docker-compose -f .\docker-compose.v1.yaml up
# minikube tunnel started other terminal
# browse to http://${TUNNEL_IP_ADDR}:58080
docker-compose -f .\docker-compose.v1.yaml down --volumes

```

### v2
```powershell
cd C:\Users\gregn\Dev\minikube\demoapp
docker-compose -f .\docker-compose.v2.yaml up
# minikube tunnel started other terminal
# browse to http://${TUNNEL_IP_ADDR}:58008 # <-- NB port
docker-compose -f .\docker-compose.v2.yaml down --volumes

```


```powershell
kubectl apply -f .\kubernetes
kubectl get all

```


# Access to LoadBalancer Service
Separate terminal
```powershell
minikube tunnel
```

```powershell
kubectl get svc -l app=frontend #  <---- note the external IP
curl http://$EXTERNAL_IP # or browser

```


# Istio
```powershell
$env:path += ";C:\Users\gregn\Dev\minikube\istio-1.7.4\bin"
cd istio-1.7.4
istioctl install --set profile=demo
kubectl label namespace default istio-injection=enabled

```


Ingress Gateway
```shell script
kubectl apply -f istio/gateway.yaml

kubectl get svc istio-ingressgateway -n istio-system

```
