# microservice_python

This is a template for a Python microservice on Kubernetes.

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

Builds the Docker image.

Execute in terminal:

```
sudo docker build -t microservice-python:latest .
```

<br>

### Push

Pushes an image or a repository to the Google Container Registry.

A Google Cloud account is needed. Replace '__public-207110__' with your own Project-ID.

Execute in terminal:

```
sudo docker tag microservice-python:latest eu.gcr.io/public-207110/microservice-python:latest
sudo docker push eu.gcr.io/public-207110/microservice-python:latest
```

<br>

### Pull

Pulls the image from the Google Container Registry.

Execute in terminal:

```
sudo docker pull eu.gcr.io/public-207110/microservice-python:latest
```

<br>

### Run

Runs the image on your local machine.

Execute in terminal:

```
sudo docker run -p 8080:8080 eu.gcr.io/public-207110/microservice-python:latest
```

<br>

### Deploy

Deploys the application to the Kubernetes cluster.

Execute in terminal:

```
kubectl create -f deploy/kubernetes
```

<br>

Check all ressources that have been created:

```
kubectl get deployments,pods,services -n microservice
```

```
NAME                             DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/microservice-python-dep   2         2         2            2           2m

NAME                                          READY     STATUS    RESTARTS   AGE
po/microservice-python-dep-6b6dbdfb44-krtl7   1/1       Running   0          2m
po/microservice-python-dep-6b6dbdfb44-rpp7x   1/1       Running   0          2m

NAME                          TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)          AGE
svc/microservice-python-svc   LoadBalancer   10.63.251.103   104.155.76.135   8080:30667/TCP   2m
```

<br>

### Delete

To delete all resources, execute the following command.

Execute in terminal:

```
kubectl delete -f deploy/kubernetes
```
