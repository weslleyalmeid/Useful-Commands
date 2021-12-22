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

**Dockerfile- MultiStage 1**
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

**Dockerfile- MultiStage 2**
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