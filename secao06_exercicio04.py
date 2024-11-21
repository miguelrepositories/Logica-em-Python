#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 4

   Tendo como dados de entrada a altura e o sexo de uma pessoa,
   construa um algoritmo que calcule seu peso ideal, utilizando
   as seguintes fórmulas:
   Para homens: (72.7 * altura) - 58
   Para mulheres: (62.1 * altura) - 44.7
'''

#Entrada
altura = float(input("Informe a medida da sua altura: "))
sexo = input("Informe o seu sexo (M / F): ")

#Processamento
sexo = sexo.upper()
if sexo == "M":
    pesoIdeal = (72.7 * altura) - 58
elif sexo == "F":
    pesoIdeal = (62.1 * altura) - 44.7

#Saída
print("Seu peso ideal é: {0:.2f}".format(pesoIdeal))