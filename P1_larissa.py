#Criar um vetor com 100 posições inteiras, separar o vetor em par e impar, somar pares e impares, mostrar a quantidade de pares e impares.

#Importando o Random para gerar o vetor Aleatório
import random

#Criando os vetores
vetor100 = [] 
vetorPares = []
vetorImpares = []

#criando variaveis
quantidadePar = 0
quantidadeImpar = 0
somaPares = 0
somaImpares = 0
indice = 0

for indice in range(100):
  vetor100.append(int(random.randint(0,100)))

#Criando o Laço de repetição para percorrer cada Linha
for indice in range(100):
  if (vetor100[indice] % 2) == 0: #Aqui estou verificando se o vetor da posição é par, ou seja, tem resto da divisão por 2 = 0 e adicionando ele ao vetorPares
    vetorPares.append(int(vetor100[indice]))
    quantidadePar = quantidadePar + 1 #Somando para mostrar quantos pares tenho no total
    somaPares = somaPares + vetor100[indice] #Somando os pares
  else: #Caso não entre no Primeiro Se, sabemos que o número da posição analisada é impar, logo entra no Else e no vetorImpares, acontecendo o mesmo de soma e da quantidade
    vetorImpares.append(int(vetor100[indice]))
    quantidadeImpar = quantidadeImpar + 1
    somaImpares = somaImpares + vetor100[indice]

#Criando a variavel que mostra o Resultado da Soma de Todos os números, não foi criada antes pois ela não pegaria a soma correta
somaTodos = somaPares + somaImpares

#Mostrando os resultados:
print(f'O vetor com 100 n�meros aleat�rios gerado s�o: \n{vetor100}\n')


print('-- Vetor Pares e quantidade de números pares --')
print(f'{vetorPares}\n\nEssa � a quantidade de n�meros Pares: {quantidadePar}\nEsse � o Resultado da Soma dos Pares: {somaPares}\n')

print('-- Vetor Impares e quantidade de n�meros impares --')
print(f'{vetorImpares}\n\nEssa � a quantidade de n�meros Impares: {quantidadeImpar}\nEsse � o Resultado da Soma dos Impares: {somaImpares}\n')

print(f'A soma de todos os valores, tanto pares quanto impares s�o: {somaTodos}')

#OBS.: o f no começo do print é o .format e o \n é o pula linha