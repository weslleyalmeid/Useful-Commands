## Tips Makefile

### Executar
```sh
make name_execution
```

### Para adicionar bash na execucao
```makefile
SHELL := /bin/bash
# or

activate_env: SHELL := /bin/bash
	. ${PWD}/name_program
```


### Dependência
```makefile

all: predict

predict: pre_process model
	python3 predict_model.py

# @ não mostra o código no terminal
model: 
    @python3 model.py

pre_process:
    python3 pre_process.py
```


### Recebendo parâmetro
```makefile
# como executar make -p=value
run:    
    mpirun --oversubscribe -np $(p) ./paralelo
```


### Criando Env e executando com Env
[ref - creat and execute env](https://earthly.dev/blog/python-makefile/)
```makefile
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
 $(PYTHON) app.py


$(VENV)/bin/activate: requirements.txt
 python3 -m venv $(VENV)
 $(PIP) install -r requirements.txt


clean:
 rm -rf __pycache__
 rm -rf $(VENV)
```