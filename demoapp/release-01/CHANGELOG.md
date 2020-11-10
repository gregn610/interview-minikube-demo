# Basic app up & running

```powershell
minikube tunnel  # <-------------- Separate terminal. Necessary for minikube with k8s service type `loadBalancer` 
kubectl apply -f .\release-01\
kubectl get svc frontend

```

Creates:
 * frontend v1 service account, service & deployment
 * backend v1 service account, service & deployment
 * services are load balancing round robin across replicaset pods
 * [demo url](http://${FRONTEND_SVC_EXTERNAL_IP}:80/) 
    - coral backend v1 API response
    - "Hello from version 1"
