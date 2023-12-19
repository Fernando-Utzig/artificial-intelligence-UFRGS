# Trabalho 1 - Aprendizado Supervisionado
* Fernando Vieira Utzig - 324861 - Turma A
* Lucas Soller da Silva - 333052 - Turma A
* Thiago Leonel Rancan Bischoff - 324856 - Turma A

# Parte 1 - Regressão Linear
## Valores iniciais de b e w
As variáves w e b ficaram com o valor 0.
## Valores iniciais de aplha e num_iterations
num_interations ficou com o valor 1000 e o alpha foi alterado para 0.01, pois com alpha >= 0.012, a reta resultante não converge. Foi necessário importar a biblioteca csv para carregar os dados do arquivo "alegrete.csv"
## Melhor erro quadrático médio obtido na implementação da regressão linear
Utilizando os valores para w, b, alpha e num_iterations citados anteriormente, o melhor erro foi 8.529433040552066.
## Conclusões
Considerando um num_interations maior, notamos que o EQM converge para 8.52.

# Parte 2 - Tensorflow/Keras
## CIFAR-10:
* Classes: 10
* Amostras: 60000
* Tamanho das imagens: 32x32x3
* Melhor acurácia: 73.84%
* Conclusão: Mesmo não obtendo uma acurácia tão alta como os outros DataSets, o CIFAR-10 obteve um salto de acurácia de mais de 50% ao aumentar o número de camadas ocultas contidas na rede. Com a inclusão de mais algumas camadas de convolução e max-pooling, obteve-se um refinamento ainda maior no resultado, atingindo o limite de acurácia de 74%.
## Cifar-100:
* Classes: 100
* Amostras: 60.000
* Tamanho das imagens: 32x32x3
* Melhor acurácia: 40.53%
* Conclusão: Datasets muito grandes, devido a sua grande variedade de classes, são mais difíceis de treinar. Mesmo aumentando significamente a quantidade de camadas da rede, e tentando extrair o máximo de sua capacidade, a acurácia não passou de 40.53%.
## MNIST:
* Classes: 10
* Amostras: 70.000
* Tamanho das imagens: 28x28x1
* Melhor acurácia: 99.28%
* Conclusão: A combinação de camadas de convolução seguida de max pooling trouxeram bons resultados para a precisão do MSINT chegando em torno de  99,28%. Testes em que foi retirado uma camada e convolução ou max pooling ou os dois reduziram a porcentagem da precisão do aprendizado. O uso do dropout em alguns testes manteve a precisão um pouco superior a testes em que dropout não foi utilizado.
## Fashion MNIST:
* Classes: 10
* Amostras: 70.000
* Tamanho das imagens: 28x28x1
* Melhor acurácia: 93.11%
* Conclusão: A obtenção de uma boa acurácia de 93.11% na Fashion MNIST pode ser atribuída a características importantes da arquitetura, como a adição de 4 camadas convolucionais com número de filtros igual a 32, 64, 128, 256. Notamos que apenas com 3 camadas convolucionais, a acurácia diminui um pouco. Além disso, sempre após uma camada convolucional, fazemos Dropout e BatchNormalization.




