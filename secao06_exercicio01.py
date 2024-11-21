#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 1

    Ler uma variável númerica n e imprimi-la somente se a mesma for
    maior que 100, caso contrário imprimi-la com o valor zero.
'''
#Entrada
n = float(input("Digite um valor númerico: "))

#Processamento
if n > 100:
    #Saída
    print("\nn = {0}".format(n))
else:
    n = 0
    #Saída
    print("\nn = {0}".format(n))
