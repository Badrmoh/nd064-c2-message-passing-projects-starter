# UdaConnect Microservices Project

[![Build/Push Docker Images](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/docker.yml/badge.svg)](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/frontend-docker.yaml)
[![Build/Push Docker Images](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/docker.yml/badge.svg)](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/ingest-consumer-docker.yaml)
[![Build/Push Docker Images](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/docker.yml/badge.svg)](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/locations-api-docker.yaml)
[![Build/Push Docker Images](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/docker.yml/badge.svg)](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/persons-api-docker.yaml)
[![Build/Push Docker Images](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/docker.yml/badge.svg)](https://github.com/Badrmoh/kafka-prod-cons-demo/actions/workflows/postgres-postgis-docker.yaml)

# Overview
<a href="https://drive.google.com/uc?export=view&id=1H1Gr_h5yJ9WabgP9QEm33HLSYTm1UY6Z"><img src="https://drive.google.com/uc?export=view&id=1H1Gr_h5yJ9WabgP9QEm33HLSYTm1UY6Z" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

# How to
1. Clone this repo and open it in the terminal

2. Run the initial configs first

```bash
kubectl apply -f deplyments/db-configmap.yaml
kubectl apply -f deplyments/db-secret.yaml
kubectl apply -f deplyments/frontend-configmap.yaml
kubectl apply -f deplyments/kafka-configmap.yaml
```

3. Start and Configure the Database and Zookeeper

```bash
kubectl apply -f deplyments/postgres.yaml
kubectl apply -f deplyments/zookeeper.yaml
db_pod=$(kubectl get po --no-headers=true -o custom-columns=":metadata.name" | grep postgres  | tr -d '\n')
sh scripts/run_db_command.sh $db_pod
```

4. Deploy the rest of deployments
```bash
kubectl apply --recursive -f deplyments/
```
