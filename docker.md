# Docker
## LinuxTips

### 1 - Instalação

```bash
curl -fsSL https://get.docker.com | bash
```


### 2 - Executando e adminitrando

**Visualizando containers e imagens**
```bash
docker ps
docker container ls

# container ativos e parados
docker container ls -a

docker image ls
```

**Executando hello-world**
```bash
docker container run -it hello-world
```
obs.: Ao executar um container inexistente, o docker client contacta o docker daemon,
que por sua vez, irá realizar o dowload da imagem no docker hub.


**Sair do container sem matar**
```
ctrl + p + q
```

**Reconectar ao container ativo**
```bash
docker attach CONTAINER_ID
```

**Rodar container em modo deamon (rodar em background)**
```bash
docker container run -d nginx 
```

**Acessar container em modo deamon e executar comando**
```bash
# com bash
docker container exec -it <container_id> bash
docker container exec -it 1978aec8a2df bash

# com comando
docker container exec -it nginx <command>
docker container exec -it nginx ls /
```

**Start, stop e restart container específico**
```bash
docker container start CONTAINER_ID
docker container stop CONTAINER_ID
docker container restart CONTAINER_ID
```

**Inspect, retorna os detalhers do container**
```bash
docker container inspect CONTAINER_ID
```

**Pause, paraliza os servicos**
```bash
docker container pause CONTAINER_ID
docker container unpause CONTAINER_ID
```


**Logs**
```bash
docker container logs -f CONTAINER_ID
```

**Removendo container**
```bash
# desativado
docker container rm CONTAINER_ID
# ativado
docker container rm -f CONTAINER_ID
```
