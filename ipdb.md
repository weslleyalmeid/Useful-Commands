### ipdb - Debugging em python

#### Instalação
[ipdb](https://pypi.org/project/ipdb/)
```shell
    pip install ipdb
```
obs.: lembrando que é necessário ter o [ipython](https://pypi.org/project/ipython/) instalado

####  breakpoint - set_trace()
```py
    import ipdb; i

    for url in self.start_urls:
        self.driver.get(url)
        
    pdb.set_trace()
```

#### Help - h (help)
```py
    ipdb> h
```

#### Listar trecho - l (list)
```py
    ipdb> l
```

#### Avança para próxima linha -  n (next)
```py
    ipdb> n
```

#### Avança por bloco -  s (step)
```py
    ipdb> s
```

#### Avança por breakpoint -  c (continue)
```py
    ipdb> c
```

#### Verificar argumentos da função - a (arguments)
```py
    ipdb> a
```

### Mostra o trajeto de execução - where  
```py
    ipdb> where
```

### Adicionar breakpoint - b (break)  
```py
    ipdb> b [number, number] or b number

    # listar breakpoints ativos
    ipdb> b
```

### Remove breakpoint - clear and cl
```py 
ipdb> clear [number, number] or clear number or clear 
```

### Ignorar breakpoint - ignore 
```py 
# bpnumber = index no b
# count = quantidade de vezes que quer ignorar
ipdb> ignore bpnumber count
```

#### Sair - q (quit)
```py 
ipdb> q
```

#### Referências

[Debugging em python (sem IDE)](http://pythonclub.com.br/debugging-em-python-sem-ide.html)

[Debugando código Python com ipdb](https://www.youtube.com/watch?v=bUqsUrEEg44)

[Live de Python #5 - Usando o Python debugger](https://www.youtube.com/watch?v=7GnHDfV6KQ8)

[ipdb-cheat-sheet](https://wangchuan.github.io/coding/2017/07/12/ipdb-cheat-sheet.html)
