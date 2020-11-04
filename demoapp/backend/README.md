# Overview

Super simple flask app. 

HTTP serves up a bit of JSON, with mimetype set right:
```json
{
  "background": "white",
  "foreground": "red"
}

```
# Usage
```shell script
docker build -t standalone.backend .
docker run -d -p 58081:80 --name=standalone.backend standalone.backend

curl http://localhost:58081/
curl http://localhost:58081/api/v1/colour.json
```

The colours can be changed with env vars:
 - `DEMO_BACKGROUND_COLOUR`
 - `DEMO_FOREGROUND_COLOUR`
 
```shell script
docker run -d -p 58081:80 --name=standalone.backend -e DEMO_FOREGROUND_COLOUR=green standalone.backend
``` 

# Cleanup
```shell script
docker kill standalone.backend
docker rm standalone.backend

docker rmi standalone.backend

```

Trigger a flask app reload by touching `/app/uwsgi.ini`

# Troubleshooting
```shell script
docker logs -f standalone.backend

docker exec -it standalone.backend bash

env | sort 
```
