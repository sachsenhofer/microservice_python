# microservice_python

This is a template to build a microservice for Python.

<br>

# Usage

__Build__

```
sudo docker build -t microservice-python:latest .
```

<br>

__Push__

(Google Cloud account needed)

```
sudo docker tag microservice-python:latest eu.gcr.io/public-207110/microservice-python:latest
sudo docker push eu.gcr.io/public-207110/microservice-python:latest
```

<br>

__Pull__

```
sudo docker pull eu.gcr.io/public-207110/microservice-python:latest
```

<br>

__Run__

```
sudo docker run -p 8080:8080 microservice-python:latest
```

<br>

__Deploy__

```
kubectl create -f deploy/kubernetes
```

<br>

__Delete__

```
kubectl delete -f deploy/kubernetes
```


