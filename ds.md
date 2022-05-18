### Pandas

#### Loc
[ref - loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
```py

# df.loc[<linha>, <coluna>]

# realizar busca
df.loc[(df['name_col'] == value) & (df['Data'] >= data_low) & (df['Data'] <= data_hight)]
df.loc[(df['name_col'] == value) & (df['Data'].between(data_low, data_hight))]


# atribuir valor
df.loc[df['name_col'] == 0, ['name_col', 'name_col']] = 0
```