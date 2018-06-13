# microservice_python

This is a template to build a microservice for Python.

<br>

# Usage

__Build:__

```
sudo docker build -t microservice-python:latest .
```

<br>

__Push:__

A Google Cloud account is needed. Replace 'public-207110' with your own Project-ID.

```
sudo docker tag microservice-python:latest eu.gcr.io/public-207110/microservice-python:latest
sudo docker push eu.gcr.io/public-207110/microservice-python:latest
```

<br>

__Pull:__

```
sudo docker pull eu.gcr.io/public-207110/microservice-python:latest
```

<br>

__Run:__

```
sudo docker run -p 8080:8080 microservice-python:latest
```

<br>

__Deploy:__

```
kubectl create -f deploy/kubernetes
```

<br>

__Delete:__

```
kubectl delete -f deploy/kubernetes
```


