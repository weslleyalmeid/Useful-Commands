# Git e Github
## Seção 2: Configurando o Git
**Para criar o nome:**

```
git config --global user.name "Name" 
```

**para criar o email:**

```
git config --global user.email "email@email.com" 
```

**Para visualizar configurações:**

``` 
git config.usarname

git config user.email

git config --list 
```

## Seção 3: Essencial do Git
Para inicializar:
é preciso estar na pasta e digitar 
``` 
git init
 ```

Para verificar status:
```
git status
```

Para adicionar arquivo:
```
git add <arquivo>
```

- *APÓS FAZER A ALTERAÇÃO AO ACESSAR O **git status**
, É NECESSÁRIO RECONHECER O ARQUIVO NOVAMENTE PARA QUE POSSA SER FEITO O **commit**, PARA ISSO FAÇA **git add '<arquivo>***

Realizando commit:
```
git commit -m "Add test.txt"
``` 
onde o -m significa que vai ser passado uma mensagem

**ORDEM:**
```
1 - git status
2 - git add <arquivo>
3 - git commit -m "mensagem"
```

**VERIFICAR DETALHES:** (git log é seu amigo, use sempre que precisar!)

	git log // para sair digite letra q
	git log --decorate 
	git log --author="Weslley" //pesquisa por nome
	git shortlog //mostra em ordem alfabetica quantos commits e quais autores
	git shortlog -sn // nome e quantidade de commit
	git log --graph // mostra atráves de gráfico
	git show <rash>
	git diff // mostra o que inseri
	git diff --name-only //mostra o nome do arquivo que foi modificado
	git commit -am // já adiciona e commita direto


**RESETAR OS ERROS:** - Fazer um return através do Git

Se não adicionou:

	git checkout test.txt

Se já adicionou:

	git reset HEAD arquivo.formato
	git reset arquivo.formato

Se Já commitou
~~~
	soft: pega as modificações e mata o commit e deixa preparado para commitar
	git reset --soft
	mixed: mata o commit e e deixa o arquivo editado precisando add e depois commitar
	git reset mixed
	hard: ignora tudo e apaga o commit
	git reset --hard
~~~
**PARA CONECTAR O GITHUB:**

primeiro se cria a chave ssh no computador, material está no favorito do google chrome.
```
    Windows ->
    ssh-keygen -t rsa -b 4096 -C "email@email.com"
    --- apertar enter pra tudo
    digitar cd .ssh enter
    fazer um more id_rsa.pub enter
    copiar e colar no github
```

Depois para conectar, pega a opção de fazer um push que fica no git, exemplo

    git remote add origin git@github.com:weslleyalmeid/nome_repositorio.git

**VERIFICAR QUAL REPOSITÓRIO ESTÁ VINCULADO**

	git remote //mostra nome da conexão
	git remote -v //mostra mais informações

**PARA ALTERAR CONECTAR AS PASTA NO GITHUB:**

	git push -u origin master // somente no primeiro push o origin pode ser alterado o nome na etapa de git remote
	git push origin master // após a primeira conexão repositório remoto é o origin e branch é o master

**CLONANDO REPOSITÓRIOS REMOTOS:**

Pegar o ssh do repositório e fazer
	
	git clone <o ssh do git> <nome da pasta>

Para ler o arquivo pode usar
	
	more nome.format

Para pegar um arquivo pode usar
	
	cat nome.fomart

**FAZENDO FORK DE UM PROJETO:**

Fork = pegar um projeto que não é seu, fazer uma cópia  dele pra você.
Procedimento, fazer um fork e realizar as contribuições que desejo e depois enviar um pull request para a pessoa responsável.
Para fazer um fork, clica no fork e seleciona o grupo, ai ele leva um cópia para outro repositório.

O QUE É UM BRANCH?

é um ponteiro móvel que leva a um commit

POR QUE USAR UM BRANCH?

Vantangens:	Poder modificar sem alterar o local principal(master)
		Facilmente "desligável"
		Múltiplas pessoasl trabalhando
		Evita conflintos

**CRIANDO UM BRANCH**

	git checkout -b <nome do branch> // criar um branch
	git branch // aparece o nome dos branchs e * selecionado
	git ckeckout <nome do branch> // seleciono o branch
	git branch -D <nome do branch> // deleta o branch

UNINDO OS BRANCHES: unir o trabalho o que cada um fez

**PASSO A PASSO DO MERGE:**

    PRO: Operação não destrutiva

    CONTRA: - Um commit a mais
	        - histórico poluido

**PASSO A PASSO DO REBASE:**

    PRO:	- evita commit extra
	        - histórico linear

    CONTRA:	- Perde a ordem cronológica

Quando quero fazer o merge/rebase
- mudo para branch que quero levar para o status "novo"
por exemplo, se a branch main e abacate estão trabalhando no mesmo projeto e o abacate adicionou uma nova feature, preciso que a main avance para esse novo estado, assim.
```sh
git checkout main ou git branch main

git merge abacate
```
Desta forma a branch atual *main* irá apontar para o mesmo ponteiro da branch *abacate*, ou seja, uniu main com abacate.

**MERGE E REBASE NA PRÁTICA**:

    merge = git merge <nome do branch>
    rebase = git rebase <nome do branch>
... Sempre que possível utilizar rebase, mas para casos
de pull request, se faz necessário o merge.
	
**PARA IGNORAR UM ARQUIVO:** `.gitinore`

Criar um arquivo .gtignore na pasta atual, colocar o nome da extenção ou do arquivo, por exemplo
* .json
arquivo.json
o gitignore, ele ignora esse arquivo nas operações do git, bastante utilizado quando não se quer upar senhas para o git.

**GIT STASH:**

Exemplo, quando estou trabalhando em um arquivo em uma branch e desejo ir para outro bransh porém não posso perder o que foi feito no atual arquivo e também não posso commitar a edição no novo branch, para isso utilizar
`git stash`
ele salva o arquivo na situação work progresso, após você fazer as modificações.

Para recuperar execute

	git stash apply
	git stash list // mostra todos stash em aberto
	git stash clear // limpa tudo

**PARA GIT ALIAS, OU SEJA ABREVIAR NOME:**

	git config --global alias.(atalho que quero) (comando que quero)

exemplo:

	git status
	git config --global alias.s status

para desfazer

	git config --global --unset alias.nome_do_alias

exemplo do caso acima

	git config --global --unset alias.s

para ver alias criados

	git config --list

**VERSIONAMENTO COM TAGS:**

	git tag -a 1.0.0 -m "mensagem"

após adicionado tag, fazer push pro git

	git push origin master --tags
verificando no git se é alterado o release onde aparece a versão

	git tag // aparece todas as tags

**GIT REVERT**

Após inserir algo e subir pra produção e o sistema parar de funcionar,
pegue o hash atráves do

	git log
para reverter a situação faça

	git revert hash

Porque usar revert? Supondo que você está trabalhando em algo absurdamente grande, tu revert a situação no sistema, mas depois você pode dar um checkout no commit estragado para tentar solucionar o que aconteceu, ou seja, não perder do histórico as mudanças que foram feitas


**APAGAR TAGS E BRANCHS REMOTOS**

	git push origin :n° tag
exemplo:

    git push origin :1.0.0
para branchs:

	git push origin :nome branch


## Anotações úteis

**Voltar estado anterior após pull**
[ref - voltar estado anterior](https://stackoverflow.com/questions/1223354/undo-git-pull-how-to-bring-repos-to-old-state)
```sh
# encontrar hash do estado anterior
git reflog
# onde a0d3fe6 representa a hash do estado anterior
git reset --hard a0d3fe6

# se quiser voltar ao penúltimo commit
git reset --hard HEAD~1

# volta ao estado anterior e mantem a alteração
git reset mixed HEAD~1
```

**Voltar a commit anterior**
```sh
# encontrar hash do commit
git log

# criar branch apontando para o commit
git checkout hash_commit
```

**Verificar se existe alteração no repo remoto**
[ref - sobre branch origin/main](https://stackoverflow.com/questions/18137175/in-git-what-is-the-difference-between-origin-master-vs-origin-master)
```sh
# git fetch name_remote/name_branch, 
# lembrando como origin/main é uma branch mesclado a branch origin e main

git fetch origin/main


# verificar apenas arquivos alterados, sem --name-only, aparece as diferenças dos arquivos
git diff origin/main --name-only

# se quiser mesclar alterações do remoto para local
git merge origin/main

# se não quiser verificar e já mesclar direto
git pull
```


**Verificar Logs in Árvores**
[ref - logs](https://stackoverflow.com/questions/1064361/unable-to-show-a-git-tree-in-terminal)
```sh
git log --graph --oneline --all
git log --graph --decorate --pretty=oneline --abbrev-commit
git log --oneline --decorate --all --graph
```

**Verificar arquivos ignorados pelo .gitignore**
[ref - check ignore files](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)
```sh
git status --ignored
```

**Verificar arquivos não trackeados**
[ref - check ignore files](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)
```sh
git status -uall
```


**Submodulos**
```sh
# criar submodulos
touch .gitmodule
git submodule add repo_clone
git add repo_name
git commit -m 'blabla'
git push origin branch


# clonar repo com submodulos
git clone --recursive repo_url

# pull
git pull --recurse-submodules

# para não especificar flag submodelus
git config submodule.recurse true

# inicializar submodule
git update submodule --init 
```

**detectar bug "automaticamente"**
[ref - bisect](https://youtu.be/wYSqDiIvCw4)
```sh
# inicia a randomização da escolha do commit
git bisect start

# apos testar o commit atual, falar se é bad
git bisect bad

# quando encontrado commit sem erro, aplicar o good
git bisect good

# quando encontrado o commit com erro, mostrar as alterações
git show


# voltar para onde estava antes do start
git bisect reset
```

**Problemas com Tracking**
```sh
git push -u <remote> <branch>
git push -u origin weslley

git branch --set-upstream-to=origin/<nome_branch_remota> nome_branch__local
git branch --set-upstream-to=origin/weslley weslley
```

