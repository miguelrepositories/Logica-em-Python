#-*- coding: UTF-8 -*-
'''Seção 07 - Exercício 2

   Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10
   emita uma mensagem: "Múltiplo de 10". 
'''
for i in range(1, 101):
    print(i)
    if i % 10 == 0:
        print("^ Múltiplo de 10.")