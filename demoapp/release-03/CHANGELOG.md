# Dark deploy v2 backend
```powershell
kubectl apply -f .\release-03\
kubectl get deployment

```

Creates:
 * New deployment & pods for v2 backend
 * Ready for dark testing
```powershell
kubectl get pods
kubectl exec -it backend-deployment-v2-66cfb95597-99dn9 -- bash
```
```shell script
wget -q -O - http://localhost/api/v1/colour.json
```
```console
{
  "background": "white",
  "foreground": "khaki"
}
```