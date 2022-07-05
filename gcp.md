
# Google Cloud Platform

### 1 - GSutil
**Preparando ambiente**
```sh
# verificar bucket
gsutil ls gc://name_bucket

# copiar arquivos para o bucket
gsutil cp earthquakes.* gs://hello-world2022


# ver head dos dados
gsutil cat gs://movielens-demo/movies.csv | head
```

**Listandos blobs**
```py
from google.cloud import storage
# Instantiates a client
storage_client = storage.Client()
# Get GCS bucket
bucket = storage_client.get_bucket(bucket_name)
# Get blobs in bucket (including all subdirectories)
blobs_all = list(bucket.list_blobs())
# Get blobs in specific subirectory
blobs_specific = list(bucket.list_blobs(prefix='path/to/subfolder/'))


# listando blobs com o prefixo
blobs_all = bucket.list_blobs(prefix='path/to/subfolder/')
set(blobs_all)
blobs_all.prefixes
```

### 2 - GCloud
```sh
# fazer login
gcloud auth login
gcloud auth application-default login

# definir projeto
gcloud config set project project_id


# listar projetos
gcloud projects list
gcloud projects list --sort-by=projectId --limit=5


# criar instancia sql
gcloud sql instances create my-database3 --region=us-central1;


# criar database
gcloud sql databases create movielens --instance=my-database3

# connectar no sql
gcloud sql connect my-database3 -u root

# importantdo a tabela ratings
gcloud sql import csv my-database=movielens --table=ratings
```

### 3 - BQ
```sh
# conectar bq no sql google, api bq connection api
    bq mk --connection --display_name='friendly name' --connection_type=TYPE \
      --properties=PROPERTIES --connection_credential=CREDENTIALS \
      --project_id=PROJECT_ID --location=LOCATION \
      CONNECTION_ID
```

- TYPE: o tipo da fonte de dados externa.
- PROPERTIES: os parâmetros da conexão criada no formato JSON.    
  - Por exemplo, --properties='{"param":"param_value"}'. Para criar um recurso de conexão, é necessário fornecer os parâmetros instanceID, database e type.
- CREDENTIALS: os parâmetros username e password.
- PROJECT_ID: o ID do projeto;
- LOCATION: a região em que a instância do Cloud SQL está localizada.
- CONNECTION_ID: o identificador de conexão

Exemplo de query
```sql
# Tem que usar o EXTERNAL_QUERY
SELECT c.customer_id, c.name, rq.first_order_date
FROM mydataset.customers AS c
LEFT OUTER JOIN EXTERNAL_QUERY(
  'us.connection_id',
  '''SELECT customer_id, MIN(order_date) AS first_order_date
  FROM orders
  GROUP BY customer_id''') AS rq ON rq.customer_id = c.customer_id
GROUP BY c.customer_id, c.name, rq.first_order_date;
```