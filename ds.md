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