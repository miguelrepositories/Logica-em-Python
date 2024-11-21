#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 8

    Faça um algoritmo que leia um número inteiro e mostre uma mensagem
    indicando se este número é par ou ímpar, e se é positivo ou negativo.
'''
import sys

#Entrada
num = int(input("Digite um número inteiro: "))
parImpar = "par"
posOuNeg = "positivo"

#Processamentos
if num == 0:
    #Saída
    print("\nO número digitado é neutro.")
    sys.exit()
elif num % 2 == 0:
    parImpar = "par"
elif num % 2 != 0:
    parImpar = "ímpar"
if num > 0:
    posOuNeg = "positivo"
elif num < 0:
    posOuNeg = "negativo"

#Saída
print("\nO número digitado é {0} e {1}.".format(parImpar, posOuNeg))
    