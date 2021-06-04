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
apos instalado lembrar de inicializar em _settings_ no campo INSTALLED_APPS 

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


Criando as classes
```python
    class Evento(models.Model):
        # Campo varchar limitado
        titulo = models.CharField(max_length=100)
        # Campo texto ilimitado
        descricao = models.TextField(blank=True, null=True)
        # verbosidade customiza o nome que aparece no front
        data_evento = models.DateTimeField(verbose_name='Data do Evento')
        # Inserete automaticamente a data atual
        data_criacao = models.DateTimeField(auto_now=True)
```
Criando classes no models no app especifico
```
    python manage.py makemigrations core
```

Gerando o migrate especifico para visualizar a saida em SQL
```
    python manage.py sqlmigrate core 0001
```

Persistindo operação migrate no banco de dados
```
    python manage.py migrate core 0001
```


Após migrado é necessário registrar no admin.py do migrations.
Para personalizar as informações é necessário adicionar o seguinte campo em admin.py
```python
    class EventoAdmin(admin.ModelAdmin):
        list_display = ('titulo', 'data_evento', 'data_criacao')

    admin.site.register(Evento, EventoAdmin)

```

para vincular uma chave extrangeira é necessario fazer o import do Users padrão do Django
```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    # Campo varchar limitado
    titulo = models.CharField(max_length=100)
    # Campo texto ilimitado
    descricao = models.TextField(blank=True, null=True)
    # verbosidade customiza o nome que aparece no front
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    # Inserete automaticamente a data atual
    data_criacao = models.DateTimeField(auto_now=True)

    # Se o usuario for deletado, exlcluir todos os eventos e dependentes dele vai ser excluido
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # nome da tabela no banco de dados
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

```

Após alterado o arquivo models é necessário atualizar o banco.
Primeiro será verificado se há alteração no migrations com o comando
```bash
    python manage.py makemigrations core
```
escolha a opção 1 e no CLI insira o valor 1, apareceu devido a necessidade do foreign key
