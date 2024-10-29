
## Executar localmente

### kind para criar cluster

Garanta que o kind está instalado.

```sh
kind create cluster
```


### fazer deploy no kubernetes
Lembre-se de criar o deployment.yaml

k8s/deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: goapp-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: goapp
  template:
    metadata:
      labels:
        app: goapp
    spec:
      containers:
        - name: goapp
          image: gointensive
          ports:
            - containerPort: 8888
```

```sh
kubectl apply -f k8s
```

verificar se pod está em execução

```sh
kubectl get pods
```
