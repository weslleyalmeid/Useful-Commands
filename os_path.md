# Comandos úteis de 'os.path' e 'os'

## Métodos de verificação

**Para verificar se é um diretório:**

	os.path.isdir('nome_arquivo')

**Verificar se é um arquivo:**

	os.path.isfile('nome_arquivo')

**Verificar se tem um diretório ou arquivo:**

	os.path.exists('nome_arquivo')

**Verifica o tamanho do arquivo em bits:**

	os.path.getsize(nome_arquivo)

## Métodos de diretórios, nomes e tipos

**Separa diretório de arquivo:**

	os.path.split('/dir1/dir2/arquivo')

**União:**

	os.path.join('dir1', 'dirN', 'arquivo')

**Obter o diretório do arquivo atual:**

	os.path.dirname('dir1/dir2/arquivo')

**Obter apenas o nome do arquivo:**

	os.path.basename('dir1/dir2/arquivo')

**Obter nome do arquivo e extenção:**

	os.path.splitext('arquivo.tipo')

**[Comum no Windows] Obter o diretório padrão:**

	os.path.normpath('dir1/dir2\arquivo')

 ## Métodos de caminhos absolutos

**Localizar diretório atual:**

	os.path.abspath('')
	os.path.abspath('.')
	os.path.abspath('__file__')

**Localizar diretório repassado:**

	os.path.abspath('dir')

**Localizar o diretório pai:**

	os.path.abspath('..')

## Adicionais


 **diretório de trabalho atual**

 	os.getcwd()
 
**remove = remove um arquivo**

	os.remove('arquivo')


**rename = renomeia um arquivo**

	os.rename('arquivo', 'renomeado')


**pathsep = separador de caminhos**

	os.pathsep

**sep = separador de diretórios**

	os.sep

**pardir = caminho de volta para diretório**

	os.pardir

**curdir = código para obter diretório atual**

	os.curdir

**linesep = separador de linhas**

	os.linesep



