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
Classes: 10\r\n
Amostras: 60000\r\n
Tamanho das imagens: 32x32x3\r\n
Melhor acurácia: 73.84%\r\n
## Cifar-100:
Classes: 100
Amostras: 60.000
Tamanho das imagens: 32x32x3
Melhor acurácia: 40.53%
## MNIST:
Classes: 10
Amostras: 70.000
Tamanho das imagens: 28x28x1
Melhor acurácia: 99.28%
## Fashion MNIST:
Classes: 10
Amostras: 70.000
Tamanho das imagens: 28x28x1
Melhor acurácia:
