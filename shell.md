## Comandos mais utilizados em Shell

**acessar manual**:

	man comando

**Criar arquivo**:

	touch arquivo

**Escrita no terminal**:

	echo 'text'

**Escrita sem quebrar linha**:

	echo -n 'text'

**Escrita com comandos de tabulação**:

	echo -e 'text \t text'

**Criar diretório**:

	mkdir diretorio
	mkdir -p pasta1/dir1

**Apagar arquivo**:

	rm arquivo

**Apagar diretório rm**:

	rm -r diretorio
	rm -f diretorio
	rm -rf diretorio

**Temporizador sleep**:

	sleep time

**Mostrar na tela comando cat**:

	cat arquivo
	cat -b arquivo [enumerar a linha]
	cat -n arquivo [enumerar todas as linhas]
	cat -A arquivo [mostrar caracteres especiais]

**mostrar na tela comando invertido tac**:

	tac arquivo

**mostrar ultimas linhas tail**:

	tail -n3 arquivo 

**mostrar primeiras linhas head**:

	head -n5 arquivo
	head -c5 arquivo

**contar linhas, palavras e caracteres wc**:

	wc arquivo
	wc -l arquivo [linhas]
	wc -w arquivo [palavras]
	wc -m arquivo [caracteres]
	wc arquivo* [busca todos arquivos]

comando pipe |

	comando arquivo | comando
	tail -n10 arquivo | wc -m [exemplo]

**comando ordenação sort**:

	sort arquivo
	sort -r arquivo [reverso] 
	sort -k2 arquivo [ordernar por outro campo]
	**sort -k3 -t'**:' [passando parâmetro separados string]
	**sort -k3 -t'**:' [passando parâmetro separados numérico]

**comando uniq**:

	uniq arquivo
	uniq arquivo -u [só os que apareceram 1 vez]
	uniq arquivo -d [só os que apareceram +1 vez]
	uniq arquivo -c [conta as repetições]

**comando tr**:

	command | tr expressão expressão [estilo replace]
	command | tr -d expressão [deletar]
	command | tr -s expressão [comprimi caracter repetido]

**comando cut**:

	command | cut -cN-N+ [c1=5 mosta de colun 1 a 5]
	command | cut -d'seprador' -fCampo [campo]

**comando diff**:

	diff arquivo1 arquivo2 [diffenrença entre os arquivos]
	diff -w arquivo1 arquivo2 [-w ignora espaço em branco]
	diff -r dir1 dir2 [comparando diretórios]
	
**comando grep**

	grep parametro arquivo
	grep parametro arquivo* [onde o * acessa todos arquivos]
	grep -i parametro arquivo [desativa o case sensitive]
	grep -c parametro arquivo [conta as ocorrencias da palavra]
	grep -v parametro arquivo [ignora a linha onde contem parametro]
	grep -r parametro * [procura recursivamente]
	grep -l parametro * [mostra o apenas o local]
	grep -A3 parametro * [After - mostrar as 3 linhas após encontrar a palavra]
	grep -B3 parametro * [After - mostrar as 3 linhas anteriores a palavra]

	fgrep = parametro só string, não aceita ER
	grep = aceita ER simples
	egrep = aceita ER extendidas

**comando sed**

	sed '1,3 d' arquivo [deleta as linhas de  1 a 3]
	sed '/Palavra/ d' arquivo [deleta a linha onde contém a palavra]
	cat alunos2.txt | sed 's/Palavra1/Palavra2/' [substitui P1 pro P2 apenas 1 vez]
	echo "Curso Linux Shell Script Linux" | sed 's/Linux/Unix/g' [g = global, substitui tudo]

**comando more**

	more arquivo [mostrar arquivo]

**comando less**

	less arquivo [mostra arquivo com mais mecanismos]
	:/pesquisa [N - Next]
	:/pesquisa [n - Prev]
	:?pesquisa [n - N]

**comando find**

	find ./ -name arquivo [encontra onde está o arquivo pelo nome]
	find ./ -name alunos* -exec ls -l {} \; [encontra e executa uma ação]
	
**comando date**

	date [mostra a hora atual]
	date +%Comando [date +%H mostra somente a hora]
	date +%d/%m/%Y [mostra dia, mês e ano]

**comando seq**

	seq número [sequencia de número 1 a N]
	seq N M [sequencia de número N a M]
	seq N I M [sequencia de número N com Intervalo até M]

**comando expr e bc**

	expr A + B [realiza soma, importante ter espaço entre A e B]
	expr A \* B [multiplicação, importante ter a barra no operador]
	echo A + B | bc [soma, sempre tem o pipe | bc , e não tem preocupação com espaço]


## Execução sequencial de comandos shell

	date ; echo Linux ; ls
	ls alunos.txt && echo Linux [só executa o segundo se o primeiro for correto]
	ls alunos.txt && echo Linux [só executa o segundo se o primeiro tiver erro]
	( cd .. ; ls -l ) [Permanece no mesmo diretório e cria um sub-shell para retornar ls]

## Redirecionamento de Input/Output

**saída padrão**

	arquivo1 > arquivo2 [cria arquivo e grava arq1 em arq2, e sempre limpa os dados]
	arquivo1 >> arquivo2 [cria arquivo e concatena informações]

**saída de erro**

	ls -l arquivo-inválido 2> log.out [utilizar 2> para gerar saída]
	ls -l arquivo-inválido 2>> log.out [concatena saída de erro]
	ls -l alunos.txtt 2> /dev/null [não mostra o erro na tela]

**saída padrão/erro**

	ls -l arquivo > log.out 2> log-erro.out [saída para as duas situações válido e inválido]
	ls -l alunos.txt2 > log.out 2>&1 [válido ou inválido vai salvar no mesmo arquivo]

**entrada**

	cat arquivo | tr a Z [joga arquivo como entrada para o tr onde substitui a por Z]
	tr 'a' 'Z' < alunos.txt 

## Copiar do diretório
```sh
# copiar pwd para o buffer do ctrl+c
echo ${PWD} | xclip -selection clipboard

# copiar dados do arquivo
xclip -i -sel copy 'file.csv'

# copiar diretorio incluindo filename
readlink -f filename.csv

# copiar filename path para o buffer do ctrl+c
readlink -f filename.csv | xclip -selection clipboard

```

## Split em arquivos
```sh

# quantidade de linhas
wc -l name_file

# split pela quantidade de linhas
split --lines=qtd_line name_file

# split pelo numero de partes 
split -n l/number_parts name_file.txt -d name_file

split -n l/number_parts name_file.csv -d name_file --additional-suffix .csv
```

## Repetição
```sh
#!/bin/bash

name="tempo"
rm -rf $name.txt

# faça o make compilar
make compile

for i in 1 2 4 6 8 16 24; do
	# escreva o print no arquivo
    printf "Threads {$i}\n" >> $name.txt
	# salve a saida no arquivo
    ./paralelo $i >> $name.txt
    printf "\n" >> $name.txt
done
```


## Listar diretórios 
```
tree /f > tree.txt
tree /A > tree.txt

```