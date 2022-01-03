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

#deletando todos containers
docker container rm -f $(docker container ls -a -q)
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

### 3 - Dockerfile Básico

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

### 1 - Volumes
Os volumes na máquina linux fica em /var/lib/docker

**Volumes do tipo Bind**
```bash
mkdir /opt/giropops
docker container run -it --mount type=bind,src=/opt/giropops,dst=/giropops debian
```


**Volumes compartilhados**
```bash
docker volume create dbdados

docker container run -d -p 5432:5432 --name pgsql1 --mount type=volume,src=dbdados,dst=/data -e POSTGRESQL_USER=docker -e POSTGRESQL_PASS=docker -e POSTGRESQL_DB=docker kamui/postgresql

docker container run -d -p 5433:5432 --name pgsql2 --mount type=volume,src=dbdados,dst=/data -e POSTGRESQL_USER=docker -e POSTGRESQL_PASS=docker -e POSTGRESQL_DB=docker kamui/postgresql
```

**Backup dos volumes**
```bash
mkdir /opt/backup

docker container run -ti --mount type=volume,src=dbdados,dst=/data --mount type=bind,src=/opt/backup,dst=/backup debian tar -cvf /backup/bkp-banco.tar /data

#conferindo
cd /opt/backup
tar -xvf bkp-banco.tar
```

**Exemplos de comandos**
```bash
 docker container run -ti --mount type=bind,src=/volume,dst=/volume ubuntu
 docker container run -ti --mount type=bind,src=/root/primeiro_container,dst=/volume ubuntu
 docker container run -ti --mount type=bind,src=/root/primeiro_container,dst=/volume,ro ubuntu
 docker volume create giropops
 docker volume rm giropops
 docker volume inspect giropops
 docker volume prune
 docker container run -d --mount type=volume,source=giropops,destination=/var/opa  nginx
 docker container create -v /data --name dbdados centos
 docker run -d -p 5432:5432 --name pgsql1 --volumes-from dbdados -e POSTGRESQL_USER=docker -e POSTGRESQL_PASS=docker -e POSTGRESQL_DB=docker kamui/postgresql
 docker run -d -p 5433:5432 --name pgsql2 --volumes-from dbdados -e  POSTGRESQL_USER=docker -e POSTGRESQL_PASS=docker -e POSTGRESQL_DB=docker kamui/postgresql
 docker run -ti --volumes-from dbdados -v $(pwd):/backup debian tar -cvf /backup/backup.tar /data
```

### 2 - Dockerfile
**Dockerfile inicial**
```bash
# Buscar ou baixar imagem
FROM debian

# Executar comandos todos na mesma camada, contatenado com &&
RUN apt-get update && apt-get install -y apache2 && apt-get clean

# Criando variaveis de ambiente 
ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

# Colocar descricao
LABEL description="Webserver"

# Criando volume no container
VOLUME /var/www/html/

# Porta de comunicação do container
EXPOSE 80
```

**Construindo a imagem dockerfile**
```bash
# docker imagem build -tag name:version .
docker image build -t meu_apache:1.0.0 .
```

```bash
# acessando
docker container run -it meu_apache:1.0.0

# verificando processos em execucao
ps -ef

# checando se apache esta instalado
dkpg -l | grep apache
```
O apache não inicializa já em execução, com isso, será necessário adequar um novo Dockerfile.

**Dockerfile com programa em execucao**
```bash
# Buscar ou baixar imagem
FROM debian

# Executar comandos todos na mesma camada, contatenado com &&
RUN apt-get update && apt-get install -y apache2 && apt-get clean

# Criando variaveis de ambiente 
ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

# Colocar descricao
LABEL description="Webserver"

# Criando volume no container
VOLUME /var/www/html/

# Porta de comunicação do container
EXPOSE 80

# Principal processo do container em modo exec != modo shell
ENTRYPOINT ["/usr/sbin/apachectl"]

# Se nao existir ENTRYPOINT add o caminho no CMD, esse modo e chamado modo shell
# CMD /usr/sbin/apachectl -D FOREGROUND
# CMD e um comando, esta passando paramentros para o principal processo do container
CMD ["-D", "FOREGROUND"]
```

**Construindo nova imagem dockerfile**
```bash
# docker imagem build -tag name:version .
docker image build -t meu_apache:2.0.0 .
```

```bash
# acessando em modo deamon, pois esta em foreground
docker container run -d -p 8080:80  meu_apache:2.0.0
```

**Dockerfile COPY arquivo local para container**
```bash
# Buscar ou baixar imagem
FROM debian

# Executar comandos todos na mesma camada, contatenado com &&
RUN apt-get update && apt-get install -y apache2 && apt-get clean

# Criando variaveis de ambiente 
ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

# Copiar arquivo do local para container
COPY index.html /var/www/html/

# Colocar descricao
LABEL description="Webserver"
LABEL version="1.0.0"
# Criando volume no container
VOLUME /var/www/html/

# Porta de comunicação do container
EXPOSE 80

# Principal processo do container em modo exec != modo shell
ENTRYPOINT ["/usr/sbin/apachectl"]

# Se nao existir ENTRYPOINT add o caminho no CMD, esse modo e chamado modo shell
# CMD /usr/sbin/apachectl -D FOREGROUND
# CMD e um comando, esta passando paramentros para o principal processo do container
CMD ["-D", "FOREGROUND"]

```

**Construindo nova imagem dockerfile**
```bash
# docker imagem build -tag name:version .
docker image build -t meu_apache:3.0.0 .
```

```bash
# acessando em modo deamon, pois esta em foreground
docker container run -d -p 8000:80 meu_apache:3.0.0
```


**Dockerfile ADD arquivo, WORKDIR e USER**
```bash
# Buscar ou baixar imagem
FROM debian

# Executar comandos todos na mesma camada, contatenado com &&
RUN apt-get update && apt-get install -y apache2 && apt-get clean

# Criando variaveis de ambiente 
ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

# Copiar arquivo do local para container
# COPY index.html /var/www/html/

# ADD parecido com copy, add faz o download, add e melhor que copy
ADD index.html /var/www/html/

# Colocar descricao
LABEL description="Webserver"
LABEL version="1.0.0"

# executando em modo usuario especifico e nao root
USER www-data

# diretorio default ao ser iniado, vai cair direto do workdir
WORKDIR /var/www/html/

# Criando volume no container
VOLUME /var/www/html/

# Porta de comunicação do container
EXPOSE 80

# Principal processo do container em modo exec != modo shell
ENTRYPOINT ["/usr/sbin/apachectl"]

# Se nao existir ENTRYPOINT add o caminho no CMD, esse modo e chamado modo shell
# CMD /usr/sbin/apachectl -D FOREGROUND
# CMD e um comando, esta passando paramentros para o principal processo do container
CMD ["-D", "FOREGROUND"]

```

**Construindo nova imagem dockerfile**
```bash
# docker imagem build -tag name:version .
docker image build -t meu_apache:4.0.0 .
```

```bash
# acessando em modo deamon, pois esta em foreground
docker container run -d -p 8008:80 meu_apache:4.0.0

# checando e nao consta, verificando erro exit(1)
docker container ls -a

# verificando log do container
docker container logs -f  ebd6
```
Foi verificado no log que o usuario não tem permissão para acessar alguns diretórios, alterado Dockerfile alterando as permissões do usuário.

**Dockerfile ADD arquivo, WORKDIR e USER com Alteracao de permissao de usuario**
```bash
# Buscar ou baixar imagem
FROM debian

# Executar comandos todos na mesma camada, contatenado com &&
RUN apt-get update && apt-get install -y apache2 && apt-get clean

# Alterando permissao do usuario
RUN chown www-data:www-data /var/lock/ && chown www-data:www-data /var/run/ && chown www-data:www-data /var/log/

# Criando variaveis de ambiente 
ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

# Copiar arquivo do local para container
# COPY index.html /var/www/html/

# ADD parecido com copy, add faz o download, add e melhor que copy
ADD index.html /var/www/html/

# Colocar descricao
LABEL description="Webserver"
LABEL version="1.0.0"

# executando em modo usuario especifico e nao root
USER www-data

# diretorio default ao ser iniado, vai cair direto do workdir
WORKDIR /var/www/html/

# Criando volume no container
VOLUME /var/www/html/

# Porta de comunicação do container
EXPOSE 80

# Principal processo do container em modo exec != modo shell
ENTRYPOINT ["/usr/sbin/apachectl"]

# Se nao existir ENTRYPOINT add o caminho no CMD, esse modo e chamado modo shell
# CMD /usr/sbin/apachectl -D FOREGROUND
# CMD e um comando, esta passando paramentros para o principal processo do container
CMD ["-D", "FOREGROUND"]
```

```bash
# acessando em modo deamon, pois esta em foreground
docker container run -d -p 8008:80 meu_apache:4.0.0
```

**Dockerfile - MultiStage 1**
```bash
# baixando a imagem Golang
FROM golang

# initial default /app
WORKDIR /app

# copiando tudo no nivel absoluto para o /app
ADD . /app

# executando o codigo que ira compilar o meugo
RUN go mod init meugo && go build -o meugo

# imagem com meu_go executando
ENTRYPOINT ./meugo

```

```bash
docker image build -t meugo:1.0 .
docker container run -it meugo:1.0
```

**Dockerfile - MultiStage 2**
```bash
# baixando a imagem Golang e colocando Alias
FROM golang AS buildando

# initial default /app
WORKDIR /app

# copiando tudo no nivel absoluto para o /app
ADD . /app

# executando o codigo que ira compilar o meugo
RUN go mod init meugo && go build -o meugo


#Novo from pra testar multistage
FROM alpine

WORKDIR /abacate
#copiando arquivo do from superior buildado
COPY --from=buildando /app/meugo /abacate/


# imagem com meu_go executando
ENTRYPOINT ./meugo
```

```bash
docker image build -t meugo:2.0 .
docker container run -it meugo:2.0
```

**Dockerfile - Deep Dive, Healthcheck e Docker commit**
```bash
# Buscar ou baixar imagem
FROM debian

# Executar comandos todos na mesma camada, contatenado com &&
RUN apt-get update && apt-get install -y apache2 curl
# Alterando permissao do usuario
# RUN chown www-data:www-data /var/lock/ && chown www-data:www-data /var/run/ && chown www-data:www-data /var/log/

# Criando variaveis de ambiente 
ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

# Copiar arquivo do local para container
# COPY index.html /var/www/html/

# ADD parecido com copy, add faz o download, add e melhor que copy
ADD index.html /var/www/html/

#Checando o servico
HEALTHCHECK --interval=1m --timeout=3s \
CMD curl -f http://localhost/ || exit 1

# Colocar descricao
LABEL description="Webserver"
LABEL version="1.0.0"

# executando em modo usuario especifico e nao root
# USER www-data

# diretorio default ao ser iniado, vai cair direto do workdir
WORKDIR /var/www/html/

# Criando volume no container
VOLUME /var/www/html/

# Porta de comunicação do container
EXPOSE 80

# Principal processo do container em modo exec != modo shell
ENTRYPOINT ["/usr/sbin/apachectl"]

# Se nao existir ENTRYPOINT add o caminho no CMD, esse modo e chamado modo shell
# CMD /usr/sbin/apachectl -D FOREGROUND
# CMD e um comando, esta passando paramentros para o principal processo do container
CMD ["-D", "FOREGROUND"]
```

```bash
docker image build -t meu_apache:5.0.0 .

# acessando em modo deamon, pois esta em foreground
docker container run -d -p 8080:80 meu_apache:5.0.0
```


**Dockerfile - Docker commit**
Criar uma imagem do container
```bash
# executando container
docker container run -ti ubuntu
# instalando vim e curl
apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim curl -y

# sair com ctrl + p + q = para continuar em execucao

# docker commit -m "msg" ID_CONTAINER
docker commit -m "ubuntu com vim e curl" 54711b4b7652

# docker image tag ID_IMAGEM name:version
docker image tag 61559e0dbbd2 ubuntu_vim_curl:1.0

```

**Resumo dos comandos**
```bash
ADD => Copia novos arquivos, diretórios, arquivos TAR ou arquivos remotos e os adicionam ao filesystem do container;

CMD => Executa um comando, diferente do RUN que executa o comando no momento em que está "buildando" a imagem, o CMD executa no início da execução do container;

LABEL => Adiciona metadados a imagem como versão, descrição e fabricante;

COPY => Copia novos arquivos e diretórios e os adicionam ao filesystem do container;

ENTRYPOINT => Permite você configurar um container para rodar um executável, e quando esse executável for finalizado, o container também será;

ENV => Informa variáveis de ambiente ao container;

EXPOSE => Informa qual porta o container estará ouvindo;

FROM => Indica qual imagem será utilizada como base, ela precisa ser a primeira linha do Dockerfile;

MAINTAINER => Autor da imagem; 

RUN => Executa qualquer comando em uma nova camada no topo da imagem e "commita" as alterações. Essas alterações você poderá utilizar nas próximas instruções de seu Dockerfile;

USER => Determina qual o usuário será utilizado na imagem. Por default é o root;

VOLUME => Permite a criação de um ponto de montagem no container;

WORKDIR => Responsável por mudar do diretório / (raiz) para o especificado nele;
```

### 3 - Dockerhub

**Dockerhub**
```bash
# docker image tag ID_IMAGE ID_DOCKERHUB/name_image:version
docker image tag 312b52c65964 weslleyalmeid/meu_apache:1.0.0

# realizar login, logou para sair
docker login

# subir imagem para dockerhub
# docker push ID_DOCKERHUB/name_image:version
docker push weslleyalmeid/meu_apache:1.0.0

# baixar imagem do dockerhub 
docker pull weslleyalmeid/meu_apache
```

### 4 -  Docker Registry
Registry serve para disponibilizar sua imagem em servidor proprietário

```bash
docker container run -d -p 5000:5000 --restart=always --name registry registry:2

# docker image tag ID_IMAGE IP:PORT/name_image:version
docker image tag 312b52c65964 localhost:5000/meu_apache:1.0.0

# realizado o push para o registry
docker image push localhost:5000/meu_apache:1.0.0

# baixando a imagem
docker container run -d localhost:5000/meu_apache:1.0.0
```

## LinuxTips - Day 3

### 1 - Docker Machine (Deprecated)

**Instalação**
```bash
 4809  curl -L https://github.com/docker/machine/releases/download/v0.16.1/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine
 4810  chmod +x /tmp/docker-machine
 4811  sudo cp /tmp/docker-machine /usr/local/bin/docker-machine
```

**Criar ambiente e alguns comandos básicos**
```bash
docker-machine create --driver virtualbox giropops

# verifica as informacoes de ambiente 
docker-machine env giropops
# carrega informacoes
eval $(docker-machine env giropops)

# acessa a maquina docker
docker-machine ssh giropops
docker-machine stop giropops
docker-machine start giropops
docker-machine status giropops

# deleta as informacoes
docker-machine env -u

# delete a imagem
docker-machine rm giropops
```

### 2 - Docker Swarm
Em um ambiente de gerenciamento e orquestração, é interessante a quantidade de nós de gerencia em um total
de 51%, ou seja, é melhor ter um número ímpar de nós, resumindo, é necessário mais de 50% dos managers estável
para o cluster ficar saudável.

**Criar ambiente e alguns comandos básicos**
```bash
# iniciar e copiar o token de nós no hosts externos.
docker swarm init

# iniciar com outra interface de rede
docker swarm init --advertise-addr=ip_cluster

# ver os nós
docker node ls

# promover os nós para possíveis managers
docker node promote name_node

# rebaixar os nós
docker node demote name_node


# retirar nó do cluster, manager -f
docker swarm leave
docker swarm leave -f

# get token
docker swarm join-token worker
docker swarm join-token manager

# rotacionar token
docker swarm join-token --rotate worker
docker swarm join-token --rotate manager
```

**Docker Swarm - Node**
```bash
# criar 3 servicos no clusters
docker service create --name webserver --replicas 3 -p 8080:80 nginx

# aceitar ou nao novos containers
# pause =  nao aceita novos containers
# active(default) = ativar o recebimento de container
docker node update --availability pause name_node

docker service scale webserver=10
```

**Docker Swarm - Services**
```bash
# criar 3 container e bindar portar em todos nós do cluters
docker service create --name giropops --replicas 3 -p 8080:80 nginx

# checar o servico
docker service inspect giropops --pretty

# scale up and down
docker service scale giropops=10

# checar servicos
docker service ps giropops

# log de todos os servicos
docker service logs -f giropops

# remover servico
docker service rm giropops

# criar rede overlay
docker network create -d overlay giropops

# docker service create --name giropops --replicas 3 -p 8080:80 --mount type=volume,src=giropops,dst=/usr/share/nginx/html --hostname sua_mae --limit-cpu 0.25 --limit-memory 64M --env jeferson=lindo --dns 8.8.8.8 nginx

docker service create --name nginx1 -p 8080:80 --network giropops nginx
docker service create --name nginx2 -p 8888:80 --network giropops nginx

# acessar container e chamar curl no nome do servico
docker container exec -it id_cont bash

# ao criar novo servico em rede diferente é necessario adicionar na rede giropops para comunicao
docker service create --name nginx3 -p 8880:80 --network strigus nginx

# adicionando nginx1 a rede strigus
docker service update --network-add strigus nginx1
```


**Resumo dos comandos**
```bash
 
 docker swarm init
 
 docker swarm join --token \ SWMTKN-1-100_SEU_TOKEN SEU_IP_MASTER:2377
 
 docker node ls
 
 docker swarm join-token manager
 
 docker swarm join-token worker
 
 docker node inspect LINUXtips-02
 
 docker node promote LINUXtips-03
 
 docker node ls
 
 docker node demote LINUXtips-03
 
 docker swarm leave
 
 docker swarm leave --force
 
 docker node rm LINUXtips-03
 
 docker service create --name webserver --replicas 5 -p 8080:80  nginx
 
 curl QUALQUER_IP_NODES_CLUSTER:8080
 
 docker service ls
 
 docker service ps webserver
 
 docker service inspect webserver
 
 docker service logs -f webserver
 
 docker service rm webserver

 docker service create --name webserver --replicas 5 -p 8080:80 --mount type=volume,
 src=teste,dst=/app  nginx
 
 docker network create -d overlay giropops
 
 docker network ls
 
 docker network inspect giropops
 
 docker service scale giropops=5
 
 docker network rm giropops

 docker service create --name webserver --network giropops --replicas 5 -p 8080:80 
 --mount type=volume,src=teste,dst=/app  nginx
 
 docker service update <OPCOES> <Nome_Service> 
```


## LinuxTips - Day 4

### 1 - Secrets

**Comandos básicos**
```bash
# passando a secret via terminal
echo -n "teste teste" | docker secret create secret1 -

docker secret ls
docker secret inspect secret1

# passando secret via arquivo
docker secret create name_secret file

# apagar secret
docker secret rm name_secret

# vinculando secret no serviço
# docker service create --name name_service -p 8080:80 --secret name_secret name_image 
docker service create --name nginx -p 8080:80 --secret secret2-arquivo nginx 

# para adicionar ou remover secret
docker service update --secret-add name_secret name_service
docker service update --secret-rm name_secret name_service

# secret com user e modo
docker service create --detach=false --name app --secret source=db_pass,target=password,uid=2000,gid=3000,mode=0400 minha_app:1.0

ls -lhart /run/secrets/

docker service update --secret-rm db_pass --detach=false --secret-add source=db_pass_1,target=password app
```

### 2 - Docker compose
Docker compose é utilizado quando se pensa em deploy, já consta deixa imagem, serviços, redes e volumes todos prontos, enquanto o dockerfile tem como objetivo a construção da imagem.


<p style="color:red">
Definições: <br>
Services: Conjunto de 1 ou mais containers.
<br>
Stack: Conjunto de 1 ou mais services.
</p>

**Docker compose 1**
```yaml
version: "3.7"

services:
    web:
        image: nginx
        deploy:
          replicas: 5
          resources:
            limits:
              cpus: "0.1"
              memory: 50M
          restart_policy:
            condition: on-failure
        ports:
          - "8080:80"
        networks:
          - webserver

networks:
    webserver:
```

**Compose, Stack e Services**
```bash
# docker stack deploy -c docker-compose.yaml name_stack
docker stack deploy -c docker-compose.yaml giropops

# checando stack
docker stack ps giropops

# checando servicos
docker stack services giropops

# removendo stack
docker stack rm giropops
```

**Docker compose 2**
```yaml
version: '3'
services:
    db:
        image: mysql:5.7
        volumes:
            - db_data:/var/lib/mysql
        environment:
            MYSQL_ROOT_PASSWORD: somewordpress
            MYSQL_DATABASE: wordpress
            MYSQL_USER: wordpress
            MYSQL_PASSWORD: wordpress

    wordpress:
        depends_on:
            - db
        image: wordpress:latest
        ports:
            - "8000:80"
        environment:
            WORDPRESS_DB_HOST: db:3306
            WORDPRESS_DB_USER: wordpress
            WORDPRESS_DB_PASSWORD: wordpress

volumes:
    db_data:
```


**Docker compose 3**
```yaml
version: "3.7"
services:
    web:
        image: nginx
        deploy:
            placement:
                constraints:
                    - node.labels.dc == UK
            replicas: 5
            resources:
                limits:
                    cpus: "0.1"
                    memory: 50M
            restart_policy:
                condition: on-failure
        ports:
            - "8080:80"
        networks:
            - webserver

    visualizer:
        image: dockersamples/visualizer:stable
        ports:
            - "8888:8080"
        volumes:
            - "/var/run/docker.sock:/var/run/docker.sock"
        deploy:
            placement:
                constraints: [node.role == manager]
        networks:
            - webserver

networks:
    webserver:
```

É necessário atualizar a label de um dos nós.
```bash
# docker node update --label-add dc=UK name_nó
docker node update --label-add dc=UK pop-os 
```


**Docker compose 4**
```yaml
version: "3.7"

services:
    redis:
        image: redis:alpine
        ports:
            - "6379"
        networks:
            - frontend
        deploy:
            replicas: 2
            update_config:
                parallelism: 1
                delay: 10s
                order: start-first
            rollback_config:
                parallelism: 1
                delay: 10s
                failure_action: continue
                monitor: 60s
                order: stop-first
            restart_policy:
                condition: on-failure

    db:
        image: postgres:9.4
        volumes:
            - db-data:/var/lib/postgresql/data
        environment:
            # nao recomendado, utilizando apenas para fins de estudo
            POSTGRES_HOST_AUTH_METHOD: trust
        networks:
            - backend
        deploy:
            placement:
                constraints: [node.role == manager]

    vote:
        image: dockersamples/examplevotingapp_vote:before
        ports:
            - 5000:80
        networks:
            - frontend
        depends_on:
            - redis
        deploy:
            replicas: 2
            update_config:
                parallelism: 2
            restart_policy:
                condition: on-failure

    result:
        image: dockersamples/examplevotingapp_result:before
        ports:
            - 5001:80
        networks:
            - backend
        depends_on:
            - db
        deploy:
            replicas: 1
            update_config:
                parallelism: 1
                delay: 10s
            restart_policy:
                condition: on-failure

    worker:
        image: dockersamples/examplevotingapp_worker
        networks:
            - frontend
            - backend
        deploy:
            mode: replicated
            replicas: 1
            labels: [APP=VOTING]
            restart_policy:
                condition: on-failure
                delay: 10s
                max_attempts: 3
                window: 120s
            placement:
                constraints: [node.role == manager]

    visualizer:
        image: dockersamples/visualizer:stable
        ports:
            - "8080:8080"
        stop_grace_period: 1m30s
        volumes:
            - "/var/run/docker.sock:/var/run/docker.sock"
        deploy:
            placement:
                constraints: [node.role == manager]
networks:
    frontend:
    backend:

volumes:
    db-data:
```
