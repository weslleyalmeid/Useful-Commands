# Pandas

## Loc
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

## GroupBy
[ref - groupby agg](https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.core.groupby.DataFrameGroupBy.agg.html)
```py
df.groupby('A').agg(['min', 'max'])
df.groupby('A').B.agg(['min', 'max'])

# df.groupby('grouping column').agg({'aggregating column': 'aggregating function'})
df.groupby(['A', 'D']).agg({'B': ['min', 'max'], 'C': 'sum'})

```


## Pivot Table

```py
emp.pivot_table(index='dept', columns='gender', values='salary', aggfunc='mean').round(-3)

# equivalente groupby
# df.groupby('grouping column').agg({'aggregating column': 'aggregating function'})
emp.groupby(['dept', 'gender']).agg({'salary':'mean'}).round(-3)
```
 As **colunas de agrupamento** são passadas para os parâmetros **index** e a **coluna de agregação** é passada para o **values** e a **função de agregação** é passada para o  **aggfunc**.


## Crosstab
```py
# equivalente pivot table
pd.crosstab(index=emp['gender'], columns=emp['race'], values=emp['salary'], aggfunc='mean').round(-3)
emp.pivot_table(index='gender', columns='race', values='salary', aggfunc='mean').round(-3)


# relative frequency - trás a contagem que cada gender representa baseado no race
pd.crosstab(index=emp['gender'], columns=emp['race'])

# relative frequency - trás a porcetagem que cada gender representa baseado no race
pd.crosstab(index=emp['gender'], columns=emp['race'], normalize='columns').round(2)
```

## Melt
 melt método, que tem dois parâmetros principais, **id_vars** quais são os nomes das colunas que devem permanecer verticais (e não reformuladas) e  **value_vars** quais são os nomes das colunas a serem remodeladas em uma única coluna.
```py
df.melt(id_vars='airline', value_vars=['ATL', 'DEN', 'DFW'], var_name='nome_id_vars', value_name='nome_value_vars')
 ```

## Tuplas
```py
# transformar colunas em tuplas 
df.apply(tuple, axis=1)
df['new_col'] = list(zip(df.lat, df.long))
```


## Drop
```
df.drop(df[df['Age'] < 25].index, inplace = True)
```

## Types
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

## Feature engineer
**Transformando dados numéricos em dados categóricos**
```py
pd.qcut(microdados_enem.NU_NOTA_MT, q=4,labels=['baixa','média baixa','média alta','alta'])
```

## Style
[ref - pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)
```py
# colorir toda linha que satisfaca a cláusula
color = (df_production['Saldo_a_Produzir_Acab'] > 0).map({True: 'background-color: yellow', False: ''})
df_production.style.apply(lambda s: color)

# destacar o menor valor da coluna
df_covid_rj.style.highlight_min(subset=['specific columns'])
```

## Breakline
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

## Move Columns
[ref - pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html)
```py
col = df.pop('class')
# df.insert(position, 'name_solumn', values, allow_duplicates=False)
df.insert(0, col.name, col)
```

## Index
```py
# resetar índice
df.reset_index()

# reordenar algumas colunas
df.reindex_axis(['Gold', 'Silver', 'Bronze'], axis=1)
```

## Rename columns
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

## Duplicadas
[ref - duplicated](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
```py
# return bool
df.duplicated()

# retorna as linhas duplicadas
df[df.duplicated()]
```

## Drop
[ref - drop rows](https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression)
```py
# drop rows
# df.drop(df[<some boolean condition>].index)
df.drop(df[df.score < 50].index, inplace=True)

#drop columns
df.drop(labels=['B', 'C'], axis=1)
df.drop(columns=['B', 'C'])
```

## Concat
```py
df_final = pd.DataFrame(columns = ['abacate', 'laranja', 'limao', 'value'])

for key in dict_aux.keys():  
    row = {
        'abacate': abacate[key],
        'laranja': laranja[key],
        'limao': limao[key],
        'value': valu[key]   
    }
    
    
    df_intermediaro = pd.DataFrame([row])
    
    df_final = pd.concat([df_final, df_intermediaro], ignore_index=True)
```

## Limitar valores Lower ou Upper 
```py
cols = ['a', 'b']
df[cols] = df[cols].clip(lower=0, upper=10)
```

## Pipe pandas
[ref - pipe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html)
```py
# Nested functions
abacate(
      laranja(
        limao(
            add_melancia(feira(items)),
            "address"
            ),
        "credit_card"
        )
    )

# método tradicional
feiras = feira(items)
fruit_melancia = add_melancia(feiras)
fruit_limao = limao(fruit_melancia, "address")
fruit_laranja = laranja(fruit_limao, "credit_card")
feira completa = abacate(fruit_laranja)

# equivalente
items.pipe(feira)
     .pipe(add_melancia)
     .pipe(limao, "address")
     .pipe(laranja, "credit_card")
     .pipe(abacate)
```


## np.select + .isin e np.where
[ref - Aidan Cooper](https://www.aidancooper.co.uk/pandas-anti-patterns/)

Combinação para substituir o apply em algumas situações
```py
def get_prod_country_rank(df_):
    vcs = df_["prod_country1"].value_counts()

    # numpy.select(condlist, choicelist, default=0)
    # condilist referente a ordem do choicelist por exe: [:3] -> top3
    # se posicação da condição no condlist verdadeira, atribua o valor diretamente relacionado no choicelist
    return np.select(
        condlist=(
            df_["prod_country1"].isin(vcs.index[:3]),
            df_["prod_country1"].isin(vcs.index[:10]),
            df_["prod_country1"].isin(vcs.index[:20]),
        ),
        choicelist=("top3", "top10", "top20"),
        default="other"
    )

df = df.assign(prod_country_rank=lambda df_: get_prod_country_rank(df_))
```

```py
# np.where(condition, operation, broadcast)
df = df.assign(
    adjusted_score=lambda df_: np.where(
        df_["release_year"] > 2016, df_["imdb_score"] - 1, df_["imdb_score"]
    )
)
```

## Colunas vazias para concat forçando o type
Esse processo deixa o concat mais lento, tempo similar ao append
```py
    cols = {
        'Centro': pd.Series(dtype = 'int'),
        'Codigo_Pai_Int()egrado': pd.Series(dtype = 'str'),
        'Ano': pd.Series(dtype = 'int'),
        'Mes': pd.Series(dtype = 'int'),
        'Linha_Produto': pd.Series(dtype = 'str'),
        'ABC': pd.Series(dtype = 'str'),
        'Politica_Dias': pd.Series(dtype = 'float'),
        'Estoque_Seguranca': pd.Series(dtype = 'float'),
        'RF_Demanda': pd.Series(dtype = 'float'),
        'Ind_Acelerado': pd.Series(dtype = 'float'),
        'Volume_Real_Faturado': pd.Series(dtype = 'float'),
        'Dia': pd.Series(dtype = 'float'),
        'Demanda_Anterior': pd.Series(dtype = 'float'),
        'Demanda': pd.Series(dtype = 'float'),
        'Estoque_Ideal': pd.Series(dtype = 'float'),
        'Cob_Dias_Estoque_Atual': pd.Series(dtype = 'float'),
        'Dias_Faltante_Politica': pd.Series(dtype = 'float'),
        'Check_Pedido_Continuo': pd.Series(dtype = 'str'),
        'Pedido': pd.Series(dtype = 'float'),
        'Data_Emissao_Pedido': pd.Series(dtype = 'str'),
        'Previsao_Estoque': pd.Series(dtype = 'float')
    }
    df_final = pd.DataFrame(cols)
```
-----------------------

## Mínimo Pandas
[ref - dunderdata](https://www.dunderdata.com/blog/minimally-sufficient-pandas)

### Attributes
```py
df.columns
df.dtypes
df.index
df.shape
df.T
df.values
```

### Aggregation Methods
```py
df.all()
df.any()
df.count()
df.describe()
df.idxmax()
df.idxmin()
df.max()
df.mean()
df.median()
df.min()
df.mode()
df.nunique()
df.unique()
df.sum()
df.std()
df.var()
```

### Non-Aggretaion Statistical Methods
```py
df.abs()
df.clip()
df.corr()
df.cov()
df.cummax()
df.cummin()
df.cumprod()
df.cumsum()
df.diff()
df.nlargest()
df.nsmallest()
df.pct_change()
df.prod()
df.quantile()
df.rank()
df.round()
```

### Subset Selection
```py
df.head()
df.iloc()
df.loc()
df.tail()
```

### Missing Value Handling
```py
df.dropna()
df.fillna()
df.interpolate()
df.isna()
df.notna()
df.Grouping()
df.expanding()
df.groupby()
df.pivot_table()
df.resample()
df.rolling()
df.Joining Data()
df.append()
df.merge()
df.Other()
df.asfreq()
df.astype()
df.copy()
df.drop()
df.drop_duplicates()
df.equals()
df.isin()
df.melt()
df.plot()
df.rename()
df.replace()
df.reset_index()
df.sample()
df.select_dtypes()
df.shift()
df.sort_index()
df.sort_values()
df.to_csv()
df.to_json()
df.to_sql()
df.Functions()
pd.concat()
pd.crosstab()
pd.cut()
pd.qcut()
pd.read_csv()
pd.read_json()
pd.read_sql()
pd.to_datetime()
pd.to_timedelta()
```