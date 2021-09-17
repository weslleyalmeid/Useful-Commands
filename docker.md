# Docker
## LinuxTips - Day 1

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

**Verificando estatísticas do container CPU, I/O, Memória e Redes**
```bash
docker container stats [CONTAINER ID]
```
é possível simular um stress no container, basta entrar no container bash e deixar stats aberto
seguir os passdos abaixo e monitar no stats
```bash
docker container exec -it [CONTAINER ID] bash
apt-get update && apt-get install stress
stress --help
stress --cpu 1 --vm-bytes 128M --vm 1
```

**Verificando os processos do container "htop"**
```bash
docker container top [CONTAINER ID]
```

**Limite de memória do container**
```bash
docker container run -d -m 128M --cpus 0.5 nginx
```

**Limite de CPU do container**
```bash
# 0.4 de 1 Core
docker container run --memory 64M --cpus 0.5 nginx

# update de um container existente
docker container update --memory 64M --cpus 0.4 nginx
```

### 3 - Dockerfile

**Arquivo dockerfile**
```dockerfile
# Nome da imagem
FROM debian 

# criar informacao, metadata
LABEL app="NOME" 
# criar variavel
ENV NOME="NOME_ENV" 

# no momento do build, vai executar comando na imagem
RUN apt-get update && apt-get install -y stress && apt-get clean 

# executar ação no container
CMD stress --cpu 1 --vm-bytes 64M --vm 1
```

**Construindo a imagem**
```bash
docker image build -t toskeira:1.0 .
docker image ls
docker container run -d toskeira:1.0
docker container logs -f [CONTAINER ID]
```


## LinuxTips - Day 2

**Volumes do tipo Bind**
```bash
mkdir /opt/giropops
docker container run -it --mount type=bind,src=/opt/giropops,dst=/giropops debian
```