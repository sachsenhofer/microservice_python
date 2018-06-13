# microservice_python

<br>

# Usage

## Build

```
sudo docker build -t microservice-python:latest .
```

<br>

## Push

(Google Cloud account needed)

```
sudo docker tag microservice-python:latest eu.gcr.io/public-207110/microservice-python:latest
sudo docker push eu.gcr.io/public-207110/microservice-python:latest
```

<br>

## Pull

```
sudo docker pull eu.gcr.io/public-207110/microservice-python:latest
```

<br>

## Run

```
sudo docker run -p 8080:8080 microservice-python:latest
```

<br>

## Deploy

```
kubectl create -f deploy/kubernetes
```

