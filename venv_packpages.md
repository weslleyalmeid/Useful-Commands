# Environments

## Python Env
```sh
# criar
# python3.8 -m venv name_env
python -m venv .name_env

# ativar linux e windows
source .name_env/bin/activate
.name_env/Scripts/activate

# desativar
deactivate
```


## Virtual Env
```sh
pip install virtualven
virtualenv .name_env

# criar
virtualenv .name_env --python=python3.8

# ativar linux e windows
source .name_env/bin/activate
.name_env/Scripts/activate

# desativar
deactivate
```

## Conda
```sh
# criar
conda create -n name_env python=3.9


# ativar
conda activate name_env

# desativar
conda deactivate

# lista env
conda env list

# deletar env
conda env remove -n name_env
```

## Requirements

```sh
while read requirement; do pip show $requirement | grep Version; done < requirements.txt
```


# Packpages

## Criar pacote
```sh
meu_projeto
├── setup.py
|
├── __init__.py
|
└── src
    └── app.py
```


O setup é responsável pelo metadados do pacote

Exemplo:
```py
from setuptools import setup


setup(
    name='meu_pacote',
    version='0.0.1',
    description='meu projeto 0',
    long_description='abacate',
    author='name',
    author_email='ab@cate.com',
    packages=['src'],
    python_version='>=3.9,<4.0',
    entry_points={
        'console_scripts': [
            # name = folder.name_file:name_function
            'meu-cli = src.app:cli',
        ]
    },
    install_requires=['httpx']
)
```

Para construir, distribuir e instalar esse pacote pode ser executado os seguintes comandos:
```sh
# construir
python setup.py build

# distribuir
 python setup.py sdist

# pip install wheel
python setup.py sdist bdist_wheel

# publicar
# pip install twine
twine upload --repository blabla.com.br dist/*.whl

# instalar
python setup.py install

# para instalar sdist
pip install path.tar.gz
```

# Poetry [Environments e Packpages]
[ref = Poetry Doc](https://python-poetry.org/docs/)

```sh
# instalar Poetry por vendoring
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# iniciar projeto, vai criar uma pasta com alguns diretórios
poetry new name

# para env ficar no local
poetry config virtualenvs.in-project true
```

Estrutura de gerenciamento de projeto iniciado 
```toml
[tool.poetry] # setup.py
name = "abacate_pack"
version = "0.1.0"
description = ""
authors = ["weslleyalmeid <weslley_fac@hotmail.com>"]

[tool.poetry.dependencies] # requirements.txt
python = "^3.9"
httpx = "^0.23.0"

[tool.poetry.dev-dependencies] # requirements-dev.txt
pytest = "^5.2"

[build-system] # setuptools
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```


```sh
# dentro do projeto
poetry install

# ver libs instalar, pip freeze
poetry show
poetry show --tree


# abrir a env no shell
poetry shell

# instalar dependência
poetry add name_lib
poetry add --dev name_lib

# deletar dependência
poetry remove name_lib
poetry remove --dev name_lib
```

Adicionando entry-points

```toml
[tool.poetry] # setup.py
name = "abacate_pack"
version = "0.1.0"
description = ""
authors = ["weslleyalmeid <weslley_fac@hotmail.com>"]

[tool.poetry.dependencies] # requirements.txt
python = "^3.9"
httpx = "^0.23.0"

[tool.poetry.dev-dependencies] # requirements-dev.txt
pytest = "^5.2"

[tool.poetry.scripts] # entry-points do setuptools
abacate-cli = "abacate_pack.cli:cli"

[build-system] # setuptools
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```


```sh
# executando feature adicionada no toml
poetry run abacate-cli 

# construindo o pacote
poetry build

# publicando
poetry publish --repository


# atualizar projeto
poetry update

# atualizar poetry
poetry self update


# requirements no formato antigo
poetry export > requirements.txt
```