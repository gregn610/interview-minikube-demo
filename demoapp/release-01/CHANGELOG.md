# Basic app up & running


# Build Images
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

# Deploy
```powershell
minikube tunnel  # <-------------- Separate terminal. Necessary for minikube with k8s service type `loadBalancer`
```

```powershell
kubectl apply -f .\release-01\
kubectl get svc frontend

```


# Usage

Creates:
 * frontend v1 service account, service & deployment
 * backend v1 service account, service & deployment
 * services are load balancing round robin across replicaset pods
 * [demo url](http://${FRONTEND_SVC_EXTERNAL_IP}:80/) 
    - coral backend v1 API response
    - "Hello from version 1"
    
## Scale up deployment
```powershell
kubectl scale --replicas=2 deployment frontend-deployment-v1
kubectl scale --replicas=2 deployment backend-deployment-v1


```

## Monitor logs
Multiple pods by label
```powershell
kubectl logs -f -l app=backend -c backend

```


# Inside the cluster
```powershell
wget -q -O - backend.default.svc.cluster.local/api/v1/colour.json
wget -q -O - frontend.default.svc.cluster.local/

```

