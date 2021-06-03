# Djando 


## Instalando Djando
```bash
    pip install django
```

## Iniciando novo projeto
```bash
    django-admin startproject nome_site
```

## Estrutura básica do Django
- **django-admin.py** é o utilitário de linha de comando do Django para tarefas administrativas
- **manager**
    - É um wrapper em volta do django-admin.py
    - Ele delega tarefas para o djando-admin.py
    - Responsável por colocar o pacote do projeto sys.path
    - Ele define a variável de ambiente DJANGO_SETTINGS_MODULE que então aponta para o arquivo settings.py
- **WSGI**
    - Web Server Gateway Interface
    - Plataforma padrão para aplicações web em Python
    - O Django com o comando startproject inicia uma configuração WSGI padrão para que se possa executar sua aplicação web
    - Quando se inicia a aplicação com _runserver_ é iniciado um servidor de aplicação web leve. Esse servidor é especificado pela configuração WSGI_APPLICATION
- **Settings**
    - Nele é possível configurar por exemplo apps, conexão com banco de dados, templates, time zone, cache, segurança, arquivos estátios, etc.
- **URLs**
    - É um Schema de URL
    - Responsável por gerenciar as Rotas das URLs, onde é possível configurar pra onde cada rota será executada.
    - É uma forma limpa e elegante para gerenciar URLs.
- **Views**
    - Responsável por processar e retornar uma resposta para o cliente que fez a requisição
- **Models**
    - Define o modelo de dados inteiramente em Python
    - Faz a abstração dos objetos de banco de dados para o Python, transformando todas as tabelas em classes e os acessos são feito utilizando linguagem Python, onde o Django realiza a transformação para SQL.
- **Admin**
    - Interface administrativa gera automaticamente pelo Django
    - Ele lê os metadados que estão nos models e fornece uma interface poderosa e pronta para manipulação de dados
- **Static**
    - Responsável por armazenar os arquivos estáticos
    - CSS, javascript e imagens.
- **Templates**
    - Responsável por armazenar os arquivos HTML
    - O diretório templates é diretório padrão para armazenarmos todo o conteúdo HTML da nossa aplicação


## Tabelas padrões
- Django já possui tabelas padrões que são utilizadas principalmente para parte de segurança e autenticação
- É possível criar as tabelas padrões do Django com o comando migrate
- Ao criar as tabelas padrões do Django, é necessário criar um primeiro usuário para conseguir acessar o painel Django Administration
- Para criar um primeiro usuário administrador é necessário utilizar o comando _createsuperuser_.
- As tabelas auxiliam a autenticação e também perfis de acesso.


## Projeto Agenda

Inicializando o projeto
```bash
    django-admin startproject agenda
```

incializando um app core para o projeto, é necessário estar dentro da pasta do projeto
```bash
    django-admin startapp core
```

importando database
```
    python manager.py migrate
```
em _settings.py_ fica o campo DATABASES onde pode ser configurado para outros bancos.


Criando um usuário admin
```
    python manage.py createsuperuser --username admin
```
vai ser pedido email e senha.