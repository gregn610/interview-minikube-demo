```powershell
minikube config set memory 5120
minikube start --extra-config=apiserver.service-node-port-range=1-65535
# minikube docker-env
& minikube -p minikube docker-env | Invoke-Expression

```

Filesystem access. 
Separate terminal 
```powershell
minikube mount /Users/gregn/Dev/minikube:/host_mnt/c/Users/gregn/Dev/minikube
``` 


# Docker build images
```powershell
cd backend
docker build --no-cache . -t demoapp_backend-v1
docker build --no-cache . -t demoapp_backend-v2

cd ..\frontend
docker build --no-cache . -t demoapp_frontend

```

# Using docker-compose to build the images
```powershell
cd C:\Users\gregn\Dev\minikube\demoapp
docker-compose up 
docker-compose down --volumes
docker images

```



```powershell
kubectl apply -f .\kubernetes
kubectl get all

```


# Access to LoadBalancer Services
Separate terminal
```powershell
minikube tunnel
```

```powershell
kubectl get svc  #  <---- note the external IP
curl http://$EXTERNAL_IP:58888
```