# Métricas de desempenho de modelos

## Classificação

**True Negative**: Quantidade de vezes que o modelo acertou a predição negativa conforme os dados reais. No exemplo, o classificador previu corretamente 25377 casos em que o resultado foi de transações não fraudulentas.

**False Positive**: Quantidade de vezes que o modelo previu incorretamente um resultado como positivo. No exemplo, o classificador previu, incorretamente, 4 casos em que o resultado foi fraude, sendo que a predição correta deveria ser de não fraude.

**False Negative**: Quantidade de vezes que o modelo previu incorretamente um resultado como negativo. No exemplo, o classificador previu incorretamente 22 casos em que o resultado foi de não fraude, sendo que a predição correta deveria ser fraude.

**True Positive**: Quantidade de vezes que o modelo acertou a predição positiva conforme os dados reais. No exemplo, o classificador previu corretamente 1 caso em que houve fraude.

Através das variáveis iniciais acima é possível estruturar métricas importante para análise dos resultados.

Acurácia/Accuracy: avalia a proporção de acertos em relação a todas as previsões realizadas. É obtida somando a diagonal principal da matriz e dividindo pela soma de todos os valores.

$$
Accuracy = \frac{TN + TP}{TN + TP + FN + FP}
$$

Sensibilidade/Revocação/Recall: avalia a proporção de verdadeiros positivos dentre todos os valores positivos reais. É obtida dividindo os verdadeiros positivos pela soma de positivos reais.

$$
recall = \frac{TP}{TP + FN}
$$

Precisão/Precision: avalia a proporção de verdadeiros positivos dentre as predições dadas como positivas pelo modelo. É obtida dividindo os verdadeiros positivos pela soma das previsões positivas.

$$
precision = \frac{TP}{TP + FP}
$$

F1 Score: é o equilíbrio entre a sensibilidade e a precisão, sendo a média harmônica entre as duas métricas.

$$
f1\_score = 2 * \frac{precision * recall}{precision + recall}
$$