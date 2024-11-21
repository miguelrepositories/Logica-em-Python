#-*- coding: UTF-8 -*-
'''Seção 08 - Exercício 1

  Faça um algoritmo que carregue um vetor de 5 elementos inteiros e
  em seguida armazena em um vetor apenas os números pares maiores
  que 0 (zero). No final deve mostrar os elementos do vetor na tela.
 '''
#Variáveis
vetor1 = []

#Entradas
print("Digite a seguir, 5 números inteiros.")
for i in range(5):
    n = int(input("Digite o {0}º número: ".format(i+1)))
    if n % 2 == 0 and n > 0:
        vetor1.append(n)
for i in range(0, len(vetor1)):
    print("Vetor1[{0}] = {1}".format(i, vetor1[i]))
    