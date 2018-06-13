# microservice_python

<br>

# Usage

## Build

```
sudo docker build -t microservice-python:latest .
```

## Push to Google Container Registry eu.gcr.io

```
sudo docker tag microservice-python:latest eu.gcr.io/private/microservice-python:latest
sudo docker push eu.gcr.io/private/microservice-python:latest
```

## Run

```
sudo docker run -p 8080:8080 microservice-python:latest
```
