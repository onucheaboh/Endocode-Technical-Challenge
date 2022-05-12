Minikube setup and Creation of Helm Chart 

minikube start // start the minikube cluster

Copy the env vars to be able to run docker inside minikube cluster

SET DOCKER_TLS_VERIFY=1 SET DOCKER_HOST=tcp://192.168.99.124:2376 SET DOCKER_CERT_PATH=C:\Users\onucheaboh.minikube\certs SET MINIKUBE_ACTIVE_DOCKERD=minikube

docker ps // view docker containers currently running inside minikube cluster

docker build -t flaskapp:1.0 . // Build the docker file

docker run -d -p 5000:5000 --name web flaskapp:1.0 // start the docker container

minikube ip // to get the minikube ip address

Visit 192.168.99.124 in the web browser

docker-compose build // build the docker image

docker-compose up -d // run the built image

docker-compose down // bring down the entire running docker server

// Deploy on kubernetes

cd kubernetes // cd into kubernetes folder

kubectl apply -f deployment.yml // create the kubernetes deployment

kubectl apply -f service.yml // deploy the service object

kubectl get po,svc // get the nodeport and service port


Creating our Helm Chart

- helm create template-chart

Checking that everything is OK

- helm lint .\template-chart

Creating our package file through our chart, only if we have it we can install it

- helm package .\template-chart

by installing it, as we can see from the package we created, we are installing it pointing to the correct namespace

- helm install template-chart .\template-chart-0.1.0.tgz -n helm


check that everything is running correctly

- kubectl get po $(my-namespace)

how to update? You can update any field of your chart, value.yaml, templates and so on. but after update you can create a new pack with a new version or update the one you have with the following command
- helm package .\template-chart

And to reflect it in your cluster? It is even simpler, follow this:

- helm upgrade template-chart .\template-chart-0.1.0.tgz -n helm

