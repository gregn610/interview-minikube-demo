# Add Istio service mesh

```powershell
kubectl apply -f .\release-02\
```
Creates:
 * frontend virtual service
 * Allows virtual hosts without change NGINX config
    - [http://istio-ingress.local/]()
    - [http://frontend.istio-ingress.local/]() 


Istio Service Mesh provides:
 * Routing
 * Observability
 * Blue Green or canary deployments
 * Inter-component mutual TLS, timeouts, retrys 
without changing application logic blah blah ... 
