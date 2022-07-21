# Airflow

Glossário
```
- DAG: Directed Acyclic Graph
- Hooks: Ganchos para conexões
```

## Inicialização do Ambiente

Variáveis de ambiente
```sh
export AIRFLOW_HOME=${PWD}/airflow
# ou 
export AIRFLOW_HOME=~/airflow

# Install Airflow using the constraints file
AIRFLOW_VERSION=2.3.2
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.7
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.3.1/constraints-3.7.txt
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Inicialização do airflow, atenção na inicialização, é comum apresentar erro.
```sh
airflow db init

# em ambiente local, requer cadastro do usuario
FLASK_APP=airflow.www.app flask fab create-admin

# airflow standalone
airflow webserver
airflow scheduler

# abrir localhost:8080, login e senha foram cadastrado na etapa anterior do FLASK_APP
```

## Connections

Adicionando Conexões pra API do Twitter
```md
admin > connections > create

Preencher campos:
- connection id: twitter_default
- connection type: HTTP
- host: https://api.twitter.com/
- extra: {"Authorization":"Bearer bearer_token"}
```


## Hooks

Criando Ganchos/Hooks no airflow
```
airflow > create pasta plugin > create pasta hooks > criar arquivo .py hooks
```



**Definição - Alura**
Hooks são interfaces para comunicar o DAG com recursos externos compartilhados, por exemplo, várias tarefas podem acessar um mesmo banco de dados MySQL. Assim, em vez de implementar uma conexão para cada tarefa, é possível receber a conexão pronta de um gancho.

Hooks usam conexões para ter acesso a endereço de serviços e formas de autenticação, mantendo assim o código usado para autenticação e informações relacionadas fora das regras de negócio do data pipeline.


## Operators

Todo operator vai ter um método chamado **execute**, esse método é chamado na DAG para executar a tarefa.
```py
# todo operator vai ter um método chamado execute
def execute(self, context):
    pass
```

**Definição - Alura**
Um operador possuirá três características:
1) Idempotência: Independentemente de quantas vezes uma tarefa for executada com os mesmos parâmetros, o resultado final deve ser sempre o mesmo;

2) Isolamento: A tarefa não compartilha recursos com outras tarefas de qualquer outro operador;

3) Atomicidade: A tarefa é um processo indivisível e bem determinado.

Operadores geralmente executam de forma independente, e o DAG vai garantir que operadores sejam executados na ordem correta. Quando um operador é instanciado, ele se torna parte de um nodo no DAG.

Todos os operadores derivam do operador base chamado BaseOperator, e herdam vários atributos e métodos. Existem 3 tipos de operadores:

- Operadores que fazem uma ação ou chamam uma ação em outro sistema;
- Operadores usados para mover dados de um sistema para outro;
- Operadores usados como sensores, que ficam executando até que um certo critério é atingido. Sensores derivam da BaseSensorOperator e utilizam o método poke para testar o critério até que este se torne verdadeiro ou True, e usam o poke_interval para determinar a frequência de teste.


**Ajustando o salvamento dos arquivos**
- Adicionar path_file no init
- Passar self_path para o execute


## Plugin
Classe utilizada para desenvolvimento de plugins personalizados, sendo possível desenvolver plugins nas seguintes categorias.
```md
    - name
    - source
    - hooks
    - executors
    - macros
    - admin_views
    - flask_blueprints
    - menu_links
    - appbuilder_views
    - appbuilder_menu_items
```


Para criar plugin personalizado, é necessário criar o arquivo airflow_plugin.py no diretório de plugins, o airflow 2.0 não aceita instaciar airflow.operators.nome_projeto diretamento, é necessário adicionar a pasta plugins no sys.path para localização do pacote ou criar um pacote dos operators.

**Adicionando pacote ao sys.path**
Arquivo airflow_plugin.py
```
from airflow.plugins_manager import AirflowPlugin
from operators.twitter_operator import TwitterOperator
import sys
import os

# inserir path do airflow no ambiente das libs
sys.path.insert(0,os.path.join(os.environ.get('AIRFLOW_HOME'), 'plugins'))


class AluraAirflowPlugin(AirflowPlugin):
    # normalmente e o nome da empresa/projeto
    name = "alura"
    operators = [TwitterOperator]
```

## Vinculando Spark ao Airflow
```sh
# instalar libs necessárias
pip install apache-airflow-providers-apache-spark==2.1.3
```

Criar task na dag
```py
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

twitter_transform = SparkSubmitOperator(
    task_id='transform_twitter_aluraoneline',
    application=os.path.join(
            SPARK_DIR,
            'transformation.py'
        ),
    name='twitter_transformation',
    application_args=[
        '--src', 
        os.path.join(BRONZE_DIR, 'twitter_aluraonline', 'extract_date=2022-06-05'),
        '--dest', 
        os.path.join(SILVER_DIR, 'twitter_aluraonline'),
        '--process-date',
        '{{ ds }}'
    ]
)
```


Adicionando Conexões pra API o Spark
```md
admin > connections > spark_default > edit

Preencher campos:
- connection type: Spark
- host: local
<!-- - extra: {"spark-home": "diretorio_do_spark"} -->
- extra: {"spark-home": "documents/spark-3.2.1-bin-hadoop3.2"}
```

## Airflow CLI
Executando as dags
```sh
# listando as dags
airflow dags list

# listar tarefas da dag
airflow tasks list twitter_dag

# testar tasks da dag, command layout: command subcommand dag_id task_id date
airflow tasks test twitter_dag transform_twitter_aluraonline 2021-06-07
airflow tasks test twitter_dag twitter_operator 2021-06-08
```


**Alura - Principais comandos**
```
owner - Nome do dono da tarefa, apenas para descrição.
email - Endereço de email usado para alertas. Pode ser um único email ou vários divididos por vírgula, ponto e vírgula ou uma lista de strings.
email_on_retry - Indica se um email deve ser enviado quando houver falha na reexecução de uma tarefa.
email_on_failure - Indica se um email deve ser enviado caso uma tarefa tenha falhado.
retries - Número de tentativas que uma tarefa deve tentar executar antes de falhar.
retry_delay - Tempo de espera entre tentativas de execução.
start_date - Data e hora da primeira execução do DAG.
end_date - Data e hora de término da última execução do DAG.
depends_on_past - Se True, as tarefas vão executar sequencialmente e somente quando a tarefa anterior for finalizada com sucesso.
sla - Vem de Service Level Agreement, ou Acordo de Nível de Serviço, representado por um timedelta; envia um email se qualquer execução passar deste tempo após a execução sem que tenha tido sucesso, ou seja, quanto de atraso cada execução pode ter.
execution_timeout - Máximo de tempo permitido para execução de uma tarefa; se passar deste tempo, um erro é criado, e a tarefa falha.
on_failure_callback - Uma função que é chamada quando uma tarefa falha.
on_execute_callback - Uma função que é chamada antes de uma tarefa ser executada.
on_retry_callback - Uma função que é chamada quando uma tarefa tenta executar novamente após uma falha.
on_success_callback - Uma função que é chamada quando uma tarefa finaliza com sucesso.
task_concurrency - Este é o número possível de execuções do DAG em paralelo em datas diferentes.
```


## Airflow API
[ref - documentation](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html)

[ref - astromer](https://youtu.be/WTR-YT5imrY?t=1209)

No arquivo *airflow.cfg* ajuste as seguintes variáveis.
```sh

# auth_backends mudar forma de autenticação
auth_backends = airflow.api.auth.backend.basic_auth

# controle de cabeçalhos e métodos
access_control_allow_headers = origin, content-type, accept
access_control_allow_methods = POST, GET, OPTIONS, DELETE

# testando API, obtendo todos as execuções da dag
curl -X GET http://0.0.0.0:8080/api/v1/dags/twitter_dag/dagRuns --user "admin:admin"


# executar DAG com argumento {"execution_date": "2022-07-20T23:14:23.893707+00:00"}, POST
# http://0.0.0.0:8080/api/v1/dags/twitter_dag/dagRuns

# Executando DAG pela API
# curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \
# -H 'Content-Type: application/json' \
# --user "username:password" \
# -d '{
#     "is_paused": true
# }'


curl -X POST 'http://0.0.0.0:8080/api/v1/dags/twitter_dag/dagRuns' -H 'Content-Type:application/json' --user "admin:admin" -d '{"execution_date": "2022-07-20T23:20:23.893707+00:00"}'
```

Executando DAG com python
```py
import requests
from requests.auth import HTTPBasicAuth
import json

url = 'http://0.0.0.0:8080/api/v1/dags/twitter_dag/dagRuns'
headers={'Content-Type': 'application/json'}

# "execution_date" também funciona, mas a preferência é logical_date
# caso queira passar paramentros adicione "conf": { } ao payload
payload = json.dumps({
  "logical_date": "2022-07-20T23:30:24.893707+00:00",
})
auth= HTTPBasicAuth('admin', 'admin')
response = requests.post(url=url, headers=headers, data=payload, auth=auth)
print(response.text)
```