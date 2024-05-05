# Tips Gerais

## Similaridade de palavras
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

## Exemplo de Save Model
[ref - teomewhy](https://github.com/TeoCalvo/dtona/blob/master/src/ep09/model_churn/modeling/train/modelling.py)
```py
# Salvando o modelo
model_data = pd.Series( {
    'num_features': num_features,
    'cat_features': cat_features,
    'onehot': onehot,
    'features_fit':features_fit,
    'model':rf,
    'acc_oot':auc_oot_rf,
    'acc_train':auc_train_rf,
    'acc_test':auc_test_rf,
    'cutoff':0.7
} )

model_data.to_pickle( os.path.join(MODEL_DIR, 'random_forest.pkl') )
model = pd.read_pickle(os.path.join(MODELS_DIR, "model_churn.pkl"))
model['model']
```

## Pipeline e Column Tranformer
[ref - Nicholas Renotte](https://github.com/nicknochnack/ColumnTransformerPractice)

```py

from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# faz o Pipeline automaticamente
pipeline = make_pipeline(StandardScaler(), RandomForestRegressor())
pipeline.fit(X,y)

# Pipeline customizado
custom_pipeline = Pipeline([('scaling', StandardScaler()),('rfmodel', RandomForestRegressor())])

# Numeric Features
numeric_features = select_df.drop('SalePrice', axis=1).select_dtypes(exclude='object').columns
numeric_pipeline = Pipeline([('scaler', StandardScaler())])


# Categorical Features
categorical_features = select_df.select_dtypes('object').columns
categorical_pipeline = Pipeline([('onehot', OneHotEncoder())])

# ColumnTransformer([name_action, pipeline, features])
transformer = ColumnTransformer([
    ('numeric_preprocessing', numeric_pipeline, numeric_features), 
    ('categorical_preprocessing', categorical_pipeline, categorical_features)
    ])

# Full pipeline
ml_pipeline = Pipeline([
    ('all_column_preprocessing', transformer),
    ('randforestclassifier', RandomForestRegressor())
    ])

# Train
ml_pipeline.fit(X, y)

# Predict
ml_pipeline.predict(X)
```

## Diversos
## isort
```sh
# re-order os imports no arquivo
isort -rc name_file.py

# re-order todos os imports de todos os arquivos do diretorio
isort -rc .
```

## Flake
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

## Grid/Random Search

```py


def train_model(x, y):
    models = [
            {
                'classifier': [SGDClassifier(random_state=42, alpha=0.0001, learning_rate='optimal', loss='log_loss')],
                'embedding': [TfidfVectorizer(ngram_range=(1,2), use_idf=False)],
                'embedding__use_idf': [True, False],
                'embedding__ngram_range' : [(1,1), (1,2)],
                'embedding__norm': ['l1', 'l2'],
                'classifier__loss' : ['log', 'modified_huber', 'huber'],
                'classifier__penalty' : ['l2', 'l1', 'none'],
                'classifier__learning_rate' : ['adaptive', 'optimal', 'constant', 'invscaling'],
                'classifier__alpha' : [0.0001, 0.001, 0.01, 0.1]
                'transform__remove_stop_words': [True, False],
            },
            {
                'classifier': [SGDClassifier(random_state=42, alpha=0.0001, learning_rate='optimal', loss='log_loss')],
                'embedding': [FastTextUnsupervisedTransformer(model_path=model_path)],
                'classifier__loss' : ['hinge', 'log_loss', 'log', 'modified_huber', 'huber'],
                'classifier__penalty' : ['elasticnet', 'l2', 'l1', 'none'],
                'classifier__learning_rate' : ['adaptive', 'optimal', 'constant', 'invscaling'],
                'classifier__alpha' : [0.0001, 0.001, 0.01, 0.1]
                'transform__remove_stop_words': [True, False],
            },
    ]

    pipeline = Pipeline([
        ('transform', TransformText()),
        ('embedding', 'passthrough'),
        ('classifier', 'passthrough')
    ])


    grid_search = RandomizedSearchCV(pipeline, models, scoring='f1_macro', cv=5, n_iter=10, error_score='raise', verbose=3, random_state=42)
    grid_search.fit(x, y)
    return grid_search

```


## Custom Scikit Pipeline

```py

from sklearn.base import BaseEstimator, TransformerMixin

class FastTextUnsupervisedTransformer(BaseEstimator, TransformerMixin):
  """
  Custom transformer for training a fastText unsupervised model.
  """
  def __init__(self, model_path, model_params=None):
    """
    Args:
      text_column (str): The name of the text column in the DataFrame.
      model_params (dict): Parameters for the fastText model.
    """
    self.model_params = model_params
    self.model_path = model_path
    self.model = None  # Store the trained model

  def fit(self, X, y=None):
    """
    Preprocesses text data and trains the fastText model.

    Args:
      X (pd.DataFrame): The input DataFrame.
      y (pd.Series, optional): Ignored in this unsupervised setting.
    """
    self.model = fasttext.load_model(self.model_path)
    fasttext.util.reduce_model(self.model, 10)
    return self

  def transform(self, X, y=None):
    """
    This method is not applicable for unsupervised training.
    """
    if isinstance(X, Series):
      X = X.apply(self._apply_embedding)
      X = np.array([np.array(xi) for xi in X])
      return X
    return X

  def _apply_embedding(self, X):
      return self.model[X]

```