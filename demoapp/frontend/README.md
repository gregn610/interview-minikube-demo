# Overview
Simple python3 flask app presenting an HTML web page with inline javascript to set colour.
Colour info is sourced from a restful API backend and embedded into the javascript directly. 
(This is not good architecture, it's to demo a flask app accessing restful API). 

The website HTML and uWSGI config is passed in on a volume mount of the host filesystem
ToDo: move uWSGI to a config map 


# Build
## Docker build images
```powershell
cd ..\frontend
docker build --no-cache . -t demoapp_frontend:v1
docker build --no-cache . -t demoapp_frontend:v2

cd ..
docker images

```


# Usage

Note, standalone won't have a backend API available, so won't be in colour.
```shell script
docker build -t standalone.frontend .
docker run -d -p 58080:80 --name=standalone.frontend standalone.frontend

curl http://localhost:58080/

```


# Config

## API Calls
Uses env vars, if present, or defaults as below to find the Backend restful API  
 - BACKEND_API_PROTOCOL        - default=http
 - BACKEND_SERVICE_HOST        - default=localhost
 - BACKEND_SERVICE_PORT        - default=58081
 - BACKEND_API_PATH_COLOUR     - default=api/v1/colour.json



# Cleanup
```shell script
docker kill standalone.frontend
docker rm standalone.frontend

docker rmi standalone.frontend

```

Trigger a flask app reload by touching `/app/uwsgi.ini`

# Troubleshooting
```shell script
docker logs -f standalone.frontend

docker exec -it standalone.frontend bash

env | sort 
```
