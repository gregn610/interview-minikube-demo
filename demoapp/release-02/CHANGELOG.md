# Add Istio service mesh
## Install Istio
```powershell
$env:path += ";C:\Users\gregn\OneDrive\OneDrive - NominetUK.onmicrosoft.com\Bin\istioctl-1.7.4-win"
istioctl install --set profile=demo
kubectl label namespace default istio-injection=enabled

```

## Ingress Gateway
```powershell
kubectl apply -f .\release-02\
kubectl get svc istio-ingressgateway -n istio-system
notepad C:\WINDOWS\system32\drivers\etc\hosts

```

## Rolling restart deployments
```powershell
kubectl rollout restart deployment backend-deployment-v1
kubectl rollout restart deployment frontend-deployment-v1
kubectl get pods

```

Creates:
 * frontend virtual service
 * Allows virtual hosts without change NGINX config
    - [http://istio-ingress.local/]()
    - [http://frontend.istio-ingress.local/]() 

Add Kiali for visualisation
```powershell
# pinned https://raw.githubusercontent.com/istio/istio/master/samples/addons/kiali.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/f8cb8ef4eca1ae3d9a9e81e55dfff1894774c5eb/samples/addons/kiali.yaml  # Run twice ???
kubectl apply -f .\release-02\kiali-vs.yaml
kubectl get pods -n istio-system -l app=kiali

```

### Workaround
```powershell
kubectl get pods -n istio-system -l app=kiali
kubectl -n istio-system port-forward kiali-7476977cf9-9hqzb 15029:20001

```

[http://localhost:15029/]()
admin:admin


Istio Service Mesh provides:
 * Routing
 * Observability
 * Blue Green or canary deployments
 * Inter-component mutual TLS, timeouts, retrys 
without changing application logic blah blah ... 




# Istio Install

# Troubleshooting

```powershell
istioctl proxy-status

istioctl analyze --namespace default

```

```powershell
istioctl experimental describe pod frontend-deployment-v1-6b6c88b8-67nnk
```
```console

Pod: frontend-deployment-v1-6b6c88b8-67nnk
   Pod Ports: 80 (frontend), 15090 (istio-proxy)
--------------------
Service: frontend
   Port: http-80 80/HTTP targets pod port 80
DestinationRule: frontend for "frontend"
   Matching subsets: v1
      (Non-matching subsets v2)
   Traffic Policy TLS Mode: ISTIO_MUTUAL


Exposed on Ingress Gateway http://10.109.130.114
VirtualService: frontend
   Weight 100%
   /*,
   1 additional destination(s) that will not reach this pod
```


```powershell
Invoke-WebRequest -Uri http://frontend.minikube.local:56001
```

The istio gateway EXTERNAL IP
```powershell
get svc -n istio-system istio-ingressgateway
```

```powershell
docker container ls --filter name=istio-proxy_*
```


## Uninstall Istio
```powershell
istioctl manifest generate --set profile=demo | kubectl delete -f -

```

