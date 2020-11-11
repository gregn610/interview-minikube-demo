# System 
## Start minikube
```powershell
minikube config set memory 5120
minikube config set cpus 4
minikube start --extra-config=apiserver.service-node-port-range=1-65535
minikube ip
notepad C:\WINDOWS\system32\drivers\etc\hosts
minikube dashboard

```

## Windows /etc/hosts
`notepad C:\WINDOWS\system32\drivers\etc\hosts`
```ini
172.22.15.86 minikube.local
172.22.15.86 frontend.minikube.local
172.22.15.86 backend.minikube.local
```

## docker cmd
Point docker cmd at minikube VM
```powershell
# minikube docker-env
& minikube -p minikube docker-env | Invoke-Expression

```

## NB Minikube on Windows means localhost isn't there. Use `minikube ip`

# Walkthru
1) [Basic app up & running](.\release-01\CHANGELOG.md)
2) [Add Istio service mesh](.\release-02\CHANGELOG.md)
3) [Dark deploy v2 backend](.\release-03\CHANGELOG.md)
4) [Canary Release v2 frontend](.\release-04\CHANGELOG.md)












Alternatively:
## Using docker-compose to build the images
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


##Force K8s image pull
```powershell
kubectl patch deployment backend-deployment-v1 -p (-join("{\""spec\"":{\""template\"":{\""metadata\"":{\""annotations\"":{\""date\"":\""" , $(Get-Date -Format o).replace(':','-').replace('+','_') , "\""}}}}}"))

kubectl patch deployment frontend-deployment-v1 -p (-join("{\""spec\"":{\""template\"":{\""metadata\"":{\""annotations\"":{\""date\"":\""" , $(Get-Date -Format o).replace(':','-').replace('+','_') , "\""}}}}}"))

```


## Access to LoadBalancer Service
Separate terminal. 
```powershell
minikube tunnel --cleanup

```

```powershell
kubectl get svc -l app=frontend #  <---- note the external IP
curl http://$EXTERNAL_IP # or browser

```
