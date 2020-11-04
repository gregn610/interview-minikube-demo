# Prerequisites


 * Running k8s cluster ( minikube / docker-desktop)
 * `kubectl` context configured
 * [Hashicorp Waypoint](https://www.waypointproject.io/docs/getting-started) installed
 ```shell script
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install waypoint

```

```shell script
docker pull hashicorp/waypoint:latest
waypoint install -platform=docker -accept-tos

```

# Build & Deploy Instructions

 Verify k8s configured & 
 ```shell script
export KUBECONFIG=/c/Users/gregn/.kube/config
kubectl config get-contexts
kubectl get svc
``` 

