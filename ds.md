## Pandas

### Loc
[ref - loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
```py

# df.loc[<linha>, <coluna>]

# realizar busca
df.loc[(df['name_col'] == value) & (df['Data'] >= data_low) & (df['Data'] <= data_hight)]
df.loc[(df['name_col'] == value) & (df['Data'].between(data_low, data_hight))]


# atribuir valor
df.loc[df['name_col'] == 0, ['name_col', 'name_col']] = 0

# dataframe.isin pegar o que não está contido no is in
df_new = df.loc[~(df['abacate'].isin(["X", "Y"]))]
```



### GroupBy
[ref - groupby agg](https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.core.groupby.DataFrameGroupBy.agg.html)
```py
df.groupby('A').agg(['min', 'max'])
df.groupby('A').B.agg(['min', 'max'])
df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
```


### Tuplas
```py
# transformar colunas em tuplas 
df.apply(tuple, axis=1)
df['new_col'] = list(zip(df.lat, df.long))
```


### Drop
```
df.drop(df[df['Age'] < 25].index, inplace = True)
```

### Types
**Selecionando colunas categóricas e numéricas**
```py
target = 'flag_churn' # Variável resposta!
to_remove = ['dt_ref', 'seller_city', 'seller_id', target] # Variáveis para retirar das analises

features = df_abt.columns.tolist() # Todas variáveis do dataset
for f in to_remove:
    features.remove(f) # Remove uma variável por vez, das que devem ser removidas

cat_features = df_abt[features].dtypes[ df_abt[features].dtypes == 'object' ].index.tolist()
num_features = list( set(features) - set(cat_features) )
```
```py
# também é válido combinar ambos argumentos.
df.select_dtypes(include=['float64', 'bool'])
df.select_dtypes(exclude=['int64'])
```

**Convertendo colunas**
```py
base_predicao_dez_jan['Dia_do_calendário_Ajustado'].astype('datetime64[ns]')

# int64 é possível de converter colunas com valor NULL
base_predicao_dez_jan['Dia_do_calendário_Ajustado'].astype('int64')

# 
pd.to_datetime(df['specific_column'])
```

### Feature engineer
**Transformando dados numéricos em dados categóricos**
```py
pd.qcut(microdados_enem.NU_NOTA_MT, q=4,labels=['baixa','média baixa','média alta','alta'])
```

### Style
[ref - pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)
```py
# colorir toda linha que satisfaca a cláusula
color = (df_production['Saldo_a_Produzir_Acab'] > 0).map({True: 'background-color: yellow', False: ''})
df_production.style.apply(lambda s: color)

# destacar o menor valor da coluna
df_covid_rj.style.highlight_min(subset=['specific columns'])
```

### Breakline
```py
gdf_municipio\
    .query("sigla_uf == 'SP'")\
    .to_crs(crs="ESRI:102033")\
    .assign(area = lambda df: df.geometry.area / 10000)

# é necessário o parênteses
(gdf_municipio
    .query("sigla_uf == 'SP'")
    .to_crs(crs="ESRI:102033")
    .assign(area = lambda df: df.geometry.area / 10000)
)

```

### Move Columns
[ref - pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html)
```py
col = df.pop('class')
# df.insert(position, 'name_solumn', values, allow_duplicates=False)
df.insert(0, col.name, col)
```
### Index
```py
# resetar índice
df.reset_index()

# reordenar algumas colunas
df.reindex_axis(['Gold', 'Silver', 'Bronze'], axis=1)
```

### Rename columns
```py
# exemplo com método rename
dict_columns = {
    'old_name':'new_name'
}

df.rename(columns=dict_columns, inplace = True)


# outros métodos
df.columns = df.columns
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace('old_char', 'new_char')
```

### Duplicadas
[ref - duplicated](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
```py
# return bool
df.duplicated()

# retorna as linhas duplicadas
df[df.duplicated()]
```

### Drop
[ref - drop rows](https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression)
```py
# drop rows
# df.drop(df[<some boolean condition>].index)
df.drop(df[df.score < 50].index, inplace=True)

#drop columns
df.drop(labels=['B', 'C'], axis=1)
df.drop(columns=['B', 'C'])
```

### Similaridade de palavras
[ref - thefuzz](https://github.com/seatgeek/thefuzz)

- Aplicar o fuzzywuzzy em uma base de dados
- Medir a similaridade de strings e fazer **Data Cleaning**
- Outras medidas de score
    - ratio
    - partial_ratio
    - token_sort_ratio
    - token_set_ratio
    
```py
def AplicaFuzzy(query, dados, metodo_ratio, score_corte):
    # process.extract("new york jets", choices, limit=2)
    return process.extractOne(query, choices=dados, scorer=metodo_ratio, score_cutoff=score_corte)

dataset['descrição2'] = AplicaFuzzy('Iphone 6s', dataset.descrição, fuzz.ratio, 95)[0]
```

## Diversos
### isort
```sh
# re-order os imports no arquivo
isort -rc name_file.py

# re-order todos os imports de todos os arquivos do diretorio
isort -rc .
```

### Flake
```sh
# remove imports nao utilizados
autoflake -r --in-place --remove-unused-variables .
```

## Diretórios
```py
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.abspath('.'))
GROOT_DIR = os.path.dirname(os.path.abspath('..'))

# diretorio dinamico
TABLE_DIR = os.path.join(dest, "{table_name}", f"process_date={process_date}")
TABLE_DIR.format(table_name="tweet")
```