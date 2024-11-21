#-*- coding: UTF-8 -*-
'''Seção 07 - Exercício 1

   Faça um algoritmo que determine o maior entre N números.
   A condição de parada é a entrada de um valor 0, ou seja, o algoritmo
   deve ficar calculando o maior até que a entrada seja igual a 0 (ZERO).
'''
#Entrada
maior = 0.0
num = 1.0

#Processamento
while num != 0:
    num = float(input("Digite um número qualquer: "))
    if num > maior:
        maior = num

#Saída
print("\nO maior número digitado foi: {0:.2f}".format(maior))