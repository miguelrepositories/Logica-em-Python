#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 3

   Ler um número e verificar se ele é par ou ímpar.
   Quando for par armazenar esse valor em 'p' e quando
   for ímpar armazená-lo em 'i'. Exibir 'p' e 'i' no final
   do processamento.
'''

#Entradas
num = int(input("Digite um número inteiro: "))

#Processamento
if num % 2 == 0:
    p = num
    i = 0
if num % 2 != 0:
    p = 0
    i = num 
if num == 0:
    p = 0
    i = 0
#Saídas
print("p = {0}\ni = {1}".format(p, i))