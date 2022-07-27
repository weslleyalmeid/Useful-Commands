# Métricas de desempenho de modelos
[Ref - Alura](https://cursos.alura.com.br/)

## Classificação

**True Negative**: Quantidade de vezes que o modelo acertou a predição negativa conforme os dados reais. No exemplo, o classificador previu corretamente 25377 casos em que o resultado foi de transações não fraudulentas.

**False Positive**: Quantidade de vezes que o modelo previu incorretamente um resultado como positivo. No exemplo, o classificador previu, incorretamente, 4 casos em que o resultado foi fraude, sendo que a predição correta deveria ser de não fraude.

**False Negative**: Quantidade de vezes que o modelo previu incorretamente um resultado como negativo. No exemplo, o classificador previu incorretamente 22 casos em que o resultado foi de não fraude, sendo que a predição correta deveria ser fraude.

**True Positive**: Quantidade de vezes que o modelo acertou a predição positiva conforme os dados reais. No exemplo, o classificador previu corretamente 1 caso em que houve fraude.

Através das variáveis iniciais acima é possível estruturar métricas importante para análise dos resultados.

**Acurácia/Accuracy:** avalia a proporção de acertos em relação a todas as previsões realizadas. É obtida somando a diagonal principal da matriz e dividindo pela soma de todos os valores.

$$
Accuracy = \frac{TN + TP}{TN + TP + FN + FP}
$$

**Sensibilidade/Revocação/Recall:** avalia a proporção de verdadeiros positivos dentre todos os valores positivos reais. É obtida dividindo os verdadeiros positivos pela soma de positivos reais.

$$
recall = \frac{TP}{TP + FN}
$$

**Precisão/Precision:** avalia a proporção de verdadeiros positivos dentre as predições dadas como positivas pelo modelo. É obtida dividindo os verdadeiros positivos pela soma das previsões positivas.

$$
precision = \frac{TP}{TP + FP}
$$

**F1 Score:** é o equilíbrio entre a sensibilidade e a precisão, sendo a média harmônica entre as duas métricas.

$$
f1\\_{score} = 2 * \frac{precision * recall}{precision + recall}
$$


**Curva ROC**

A curva ROC (Receiver Operating Characteristic) ou curva COR (Característica de Operação do Receptor, em português) é uma das ferramentas utilizadas para avaliar um classificador mostrando a relação entre a taxa dos verdadeiros positivos e a taxa dos falsos positivos para vários pontos de cortes diferentes. A taxa dos verdadeiros positivos representa a taxa de amostras positivas que são corretamente classificadas. Podem também receber o nome de recall ou sensibilidade e é calculada de acordo com a seguinte expressão:

$$
recall = \frac{TP}{TP + FN}
$$

A taxa de falsos positivos representa a taxa de amostras positivas que são classificadas erroneamente e é calculada de acordo com a expressão:

$$
taxa de falsos positivos = 1 - especificidade = 1 - \frac{TN}{TN + FP} = \frac{FP}{TN + FP}
$$

Então, a curva ROC mostra como o classificador se comporta para diferentes valores de threshold de acordo com a relação de verdadeiros positivos e falsos positivos.


![image](/img/07-roc.png)

Existe uma linha de referência na diagonal do gráfico que corresponde à uma linha de base e representa o caso no qual o classificador classifica aleatoriamente as classes. Através da curva em azul, é possível extrair uma métrica conhecida como AUC (Area Under the Curve) ou área sob a curva. Essa métrica varia de 0 a 1 e quanto maior o seu valor, melhor será avaliado o modelo. Mas como podemos interpretar esse gráfico?

Percebe-se que a linha representando o classificador Regressão Logística, com o nome de data 1, cresce de uma forma relativamente rápida até atingir o valor máximo da taxa de verdadeiros positivos (o recall). Isso significa que o modelo atinge 100% de classificação correta dos positivos em aproximadamente (0.2, 1) e permanece até atingir o ponto (1, 1) do gráfico.

Esse ponto no gráfico nos diz que o modelo tem 100% de taxa de verdadeiros positivos e 100% de taxa de falso negativos. Isso demonstra que o modelo classifica todas as amostras positivas corretamente e que todas as que não são positivas foram incorretamente classificadas. Então, quando o modelo chega em 100% de taxa de verdadeiros positivos e lá permanece até atingir 100% da taxa de falsos positivos, significa que o modelo consegue classificar todas as amostras positivas de forma correta, independentemente do threshold adotado.