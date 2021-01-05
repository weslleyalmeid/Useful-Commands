# Flask

### Ajustes iniciais
na sheel fazer alguns exports
~~~shell
    export FLASK_APP=pasta/app.py
    export FLASK_ENV=development
~~~

instalar o requeriments com o make
~~~shell
    make install
~~~

inicializar o banco de dados, pré configurado no cli
~~~shell
    flask create-db
~~~

inicializar o migrate
~~~shell
    flask db init
    flask db migrate -m "initial migrate"
~~~
Obs.: Lembrando que esse *dm migrate* faz um "controle" do banco de dados

Após feito alguma alteração no banco de dados é necessário aplicar o migrate e upgrade
~~~shell
    flask db migrate -m "initial migrate"
    flask db upgrade
~~~

### Fask mode project
Criar um arquivo instalável, utilizado o *setuptools*
precisa ter
__init__.py
setup.py

### Comandos shell Flask
Para ver as rotas
~~~shell
flask routes
~~~

### Estrutura do projeto
delivery
|____static
| |____js
| |____css
| |____img
|______init__.py
|____ext
| |____config
| |____auth
| |____cli
| |____api
| | |______init__.py
| |____admin
| |____site
| | |______init__.py
| | |____main.py
| | |______pycache__
| | | |____main.cpython-38.pyc
| | | |______init__.cpython-38.pyc
| |____db
|____templates
| |____about.html
| |____base.html
| |____index.html
|____app.py
|______pycache__
| |______init__.cpython-38.pyc
| |____app.cpython-38.pyc


Para facilitar o desenvolvimento na arquitetura.
[Flask Project Builder](https://cesargodoi.pythonanywhere.com/)
[Flask Project Builder - GitHub](https://cesargodoi.pythonanywhere.com/)

### Templates

- Normalmente se faz um base.html e coloca e todas as especificações para criar os blocos das seções

#### Nomeando páginas atráves dos endpoints
~~~py
    <a class="navbar-item" href="{{ url_for('site.restaurants') }}">
        Restaurante
    </a>
~~~

### DB

#### script vertabelo > slqAlchemy
~~~sh
    python vertabelo_flask_sqlalchemy.py -i vertabelo.xml -o output.py
~~~

#### Dentro da pasta ext -> Entenções
Pode ser usada uma pasta com um __init__.py ou pode ser colocado
um programa.py direto na pasta, a inicialização é chamada da mesma forma no 
app.py da raiz.

#### Migrate
- Funciona para alertar ao app sobre as alterações no banco de dados
- Ele precisa saber de todas as classes no banco de dados
~~~shell
    flask db migrate -m "initial migrate"
    flask db upgrade
~~~

#### Flask-Admin
muda a cor da barra do flask admin
~~~py
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
~~~
adicionando administrador


#### Configuração
- Instalar o dynaconf
- criar arquivo settings.toml na raiz do projeto e adicionar todas as configurações necessárias
- criar um .secrets.toml na raiz do projeto para as SECRETS KEY
- carregar o arquivo config.py do ext com 
~~~py
    from dynaconf import FlaskDynaconf
~~~
- Para carregar as extenções 
~~~py
    app.config.load_extensions("EXTENSIONS")
~~~
onde EXTENSIONS é um parâmetro que estpa no arquivo setting.toml

#### Formulários




#### WSGI

executar
~~~
    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
~~~
ou
~~~
    gunicorn wsgi:app
~~~
ou
~~~
    gunicorn -b :5000 wsgi:app
~~~ 

se apresentar erro
~~~
    sudo fuser -k 8000/tcp
~~~
comando para matar programas em aberto na porta 8000


### Compartilhando com NGROK
~~~
    ./ngrok http 5000
~~~
onde 5000 é a porta de compartilhamento do wsgi ou make run


### Deploy PythonAnyWhere

1. Nesse passo, vamos clicar no botão Open Web tab, em seguida vamos clicar no botão Add a new web app.

![image](/img/1.png)

~~~
    /home/seu_usuario/mysite/wsgi.py
~~~

2. Baixar o arquivo do github e iniciar virtualenv
![image](/img/2.png)

excluir pasta mysite default
~~~
    rm -rf mysite
~~~
baixar os arquivos
~~~
    git clone https://github.com/user/arquivo.git mysite
~~~
iniciar virtualenv
~~~
    mkvirtualenv --python=/usr/bin/python3.8 my-virtualenv
~~~

3. Ajustes específicos de inicializar
entrar na paste
~~~
    cd mysite
~~~
instalar requerimentos
~~~
    make install
~~~
criar e inicializar banco de dados sqlite
~~~
    make init-db
~~~
add admin@admin.com para gestão
~~~
    flask admin-add
~~~

4. Configurar web
![image](/img/3.png)

mudar as especificações do Code

- Configure sourcecode como /home/YOURUSER/mysite/futdata
- Configure workdir como /home/YOURUSER/mysite
- Não altere o WSGI config file

![image](/img/4.png)

- Configure virtualenv to /home/yourusername/.virtualenvs/my-virtualenv 
![image](/img/5.png)

- Configure pasta static
![image](/img/6.png)

5. Referências para deploy
[dev-to](https://dev.to/theakira/deploy-de-uma-aplicacao-flask-com-pythonanywhere-5ddk)
[codeshow](https://github.com/codeshow/flask_tutorial_pybr13/tree/cms_9_deploy/cms)
[pythonanywhere](https://help.pythonanywhere.com/pages/Flask/)
Tudo certo até então, vamos clicar no botão Next


## API
### Utilizando cURL
POST
~~~
    curl -X POST -F 'chave=valor' URL
~~~
GET
~~~
    curl 127.0.0.1:5000/transactions
~~~

#### Referências
[Flask - CodeShow](https://www.twitch.tv/collections/gRe7fj7iGBZJMQ)
[cURL - 1](https://terminalroot.com.br/2019/10/12-dicas-para-voce-usar-o-comando-curl-como-um-ninja.html)
[cURL - 2](https://www.hostinger.com.br/tutoriais/comando-curl-linux/)
