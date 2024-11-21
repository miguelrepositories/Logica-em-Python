#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 2
    
    Elabore um algoritmo que leia um número. Se positivo 
    armazene-o em 'a', se for negativo, em 'b'. No final
    mostrar o resultado.
'''
#Entrada
num = float(input("Digite um número qualquer: "))

#Processamento
if num > 0:
    a = num
    #Saída
    print("{0} é um número positivo.".format(a))
if num < 0:
    #Saída
    b = num
    print("{0} é um número negativo.".format(b))
if num == 0:
    #Saída
    print("0 é um número neutro.")