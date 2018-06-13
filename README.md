# microservice_python

This is a template to build a microservice for Python.

<br>
Checkout repository:

```
git clone https://github.com/sachsenhofer/microservice_python.git
```

<br>

# App

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<html><head></head><body>Hello World!</body></html>'

@app.route('/health')
def health():
    return '0'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
```

<br>

# Dockerfile

```
FROM ubuntu:latest
MAINTAINER Dominik Sachsenhofer "dominik@sachsenhofer.io"

RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential wget curl
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["app.py"]
```

<br>

# Usage

### Build

```
sudo docker build -t microservice-python:latest .
```

<br>

### Push

A Google Cloud account is needed. Replace 'public-207110' with your own Project-ID.

```
sudo docker tag microservice-python:latest eu.gcr.io/public-207110/microservice-python:latest
sudo docker push eu.gcr.io/public-207110/microservice-python:latest
```

<br>

### Pull

```
sudo docker pull eu.gcr.io/public-207110/microservice-python:latest
```

<br>

### Run

```
sudo docker run -p 8080:8080 eu.gcr.io/public-207110/microservice-python:latest
```

<br>

### Deploy

```
kubectl create -f deploy/kubernetes
```

To get the external IP address of the loadbalancer:

```
$ kubectl get svc microservice-python-svc -n microservice
NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)          AGE
microservice-python-svc   LoadBalancer   10.63.251.103   104.155.76.135   8080:30667/TCP   2m
```

<br>

### Delete

```
kubectl delete -f deploy/kubernetes
```


