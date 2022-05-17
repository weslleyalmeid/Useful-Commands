
# Google Cloud Platform

### 1 - Introdução

```sh
# verificar bucket
gsutil ls gc://name_bucket

# copiar arquivos para o bucket
gsutil cp earthquakes.* gs://hello-world2022
```

### 2 - Login do GCloud SDK
```sh
# fazer login
gcloud auth login
gcloud auth application-default login

# definir projeto
gcloud config set project project_id
```