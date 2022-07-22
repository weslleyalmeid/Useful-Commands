# Modelos

## Random Forest
[Ref - Alura](https://cursos.alura.com.br/)

Dentre os parâmetros que podem ser modificados no modelo Random Forest, estão o criterion e as max_features. Vamos analisar o que cada um desses parâmetros faz.

```criterion```

Tem a função de medir a qualidade das divisões dos nós das árvores de decisão. As opções possíveis para esse parâmetro são **gini** ou **entropy**.

O critério de impureza Gini,ou somente Gini, serve para medir a frequência com que um elemento escolhido aleatoriamente pode ser identificado incorretamente. Isso significa que quanto menor o valor, mais puros são os dados e menor o erro cometido. Sobre a sua equação, bem como outras utilizações dessa medida, você pode ler em Gini impurity.

O critério de entropia (ou entropy) para ganho de informação é o menor número médio de perguntas binárias (sim ou não) necessário para identificar a saída de uma fonte. Esse valor informa quão informativas são as características para serem selecionadas. Desse modo, quanto maior a entropia, maior o conteúdo da informação. Para entender mais sobre a teoria por trás da entropia para ganho de informação, você pode acessar Entropy (information theory).

```max_features```

É a quantidade máxima de variáveis que pode ser utilizada para fazer as divisões dos nós das árvores. As opções possíveis para esse parâmetro são **auto**, **sqrt** , **log2** ou valores numéricos.

Caso sejam escolhidas as opções “auto** ou “sqrt**, o número máximo de variáveis será a raiz quadrada da quantidade de variáveis de treinamento.
Escolhendo a opção “log2**, será extraído o logaritmo na base 2 da quantidade de variáveis de treinamento.
E para o caso dos valores numéricos, o número máximo de variáveis que podem ser usadas nas divisões dos nós será igual ao valor utilizado.
Todos esses hiperparâmetros citados, bem como outros utilizados no Random Forest, podem ser analisados através da documentação.

Outro ponto também tratado quando se utiliza Random Forest é a validação cruzada. Caso tenha interesse em saber mais sobre esse conceito utilizado em Machine Learning, você pode ler o artigo Conhecendo a validação cruzada.