# Spark

### 1 - Inicialização
```py
#objeto mais importate do Spark
from pyspark.sql import SparkSession
# builder: vai construir a sessão
# appName: nome util para utilizacao do logs
# getOrCreate: verificar se existe sessao ativa ou criar uma nova

spark = SparkSession\
        .builder\
        .appName('twitter_transformation')\
        .getOrCreate()
```

### 2 - Comandos de leitura

```py

# transformar para dataframe Pandas
spark.read.format("bigquery").option("query", query).option("materializationDataset", tempLocation).load()

spark.read.format("csv").load(objeto_recomendacao, inferSchema="true", header="true", sep=';').toPandas()

# ler csv direto com algumas opcoes
spark.read.option("header",True).csv('/home/weslley/Desktop/squad_keras/data/external')
spark.read.options(delimiter=',').csv("path_file")
spark.readoption("header",True).option("inferSchema",True).option(delimiter=',').csv("path")


spark.read.option('inferSchema', True).csv(path, header=True, sep=',').toPandas()



# transformar para dataframe spark
# criar dataframe em dados Row
from pyspark.sql import Row
df = rdd.map(lambda x: Row(n=x)).toDF()
```

### 3 - Comandos de visualização
```py
# df é spark.read...
# selectiona data.id da primeira linha e não comprimir
df.select('data.id').show(1, False)

# explain utilizado nos sgbds
read_df.where('created_date = "2021-06-01"').explain()

# particoes ideias sao baseados em campos que apresentam uma boa cardinalidade (datas costumam ser boas cardinalidades)
tweet_df.groupBy(f.to_date('created_at')).count().show()
```


### 4 - Níveis de informações
```py
# subiu os niveis na linha e subiu para uma nova linha cada tweet
df.select(f.explode('data')).show(1, False)
# renomear colunas com alias
tweet_df = df.select(f.explode('data').alias('tweets')).select( 'tweets.author_id',
                                                                'tweets.conversation_id',
                                                                'tweets.created_at',
                                                                'tweets.id',
                                                                'tweets.in_reply_to_user_id',
                                                                'tweets.public_metrics.*',
                                                                'tweets.text'
                                                            )

```

### 5 - Comandos de escrita
```py
# salvar arquivo csv em modo sobrescrito, adicionando header
tweet_df.write.mode('overwrite').option('header', True).csv(os.path.join(DATALAKE_DIR, 'export'))

# salvar arquivo csv em modo sobrescrito, adicionando header e reparticionar(pode ser para mais ou menos)
tweet_df.repartition(4).write.mode('overwrite').option('header', True).csv(os.path.join(DATALAKE_DIR, 'export_2'))

# coalesce transforma n reparticoes em m onde m < n
tweet_df.repartition(8).coalesce(2).write.mode('overwrite').option('header', True).csv(os.path.join(DATALAKE_DIR, 'export_3'))
```


### 6 - Comandos básicos
```py
# printar schema
tweet_df.printSchema()

# printar algumas informacoes
tweet_df.show()

# verificar o numero de particoes
tweet_df.rdd.getNumPartitions()

```



### 7 - Querys

**Exemplo 1**
```py
    tweet = spark.read.json(BASE_DIR.format(stage='silver', folder_name='tweet'))
    alura = tweet.where('author_id = "1566580880"').select('author_id', 'conversation_id')

    tweet = tweet.alias('tweet')\
        .join(
            alura.alias('alura'),
            [
                tweet.author_id != alura.author_id,
                tweet.conversation_id == tweet.conversation_id
            ],
            'left'
        )\
        .withColumn('alura_conversation', when(col('alura.conversation_id').isNotNull(), 1).otherwise(0))\
        .withColumn('reply_alura', when(col('tweet.in_reply_to_user_id') == "1566580880", 1).otherwise(0))\
        .groupBy(to_date('created_at').alias('created_date'))\
        .agg(
            countDistinct('id').alias('n_tweets'),
            countDistinct('tweet.conversation_id').alias('n_conversation'),
            sum('alura_conversation').alias('alura_conversation'),
            sum('reply_alura').alias('reply_alura'),

        )\
        .withColumn('weekday', date_format('created_date', 'E'))

    tweet.coalesce(1)\
        .write\
        .json(BASE_DIR.format(stage='gold', folder_name='twitter_insight_tweet'))
```