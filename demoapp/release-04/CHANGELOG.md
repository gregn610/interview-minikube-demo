# Canary Release frontend v2
```powershell
kubectl apply -f .\release-04\

```
Creates:
 * v2 frontend deployment
 * Istio VirtualService distributing 10% traffic to v2 and 90% to v1

Refresh [http://frontend.istio-ingress.local/]() 
 - Background now khaki
 - v2 frontend pops up on 10% of refreshes
 