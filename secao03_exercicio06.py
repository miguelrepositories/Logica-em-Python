#-*- coding: UTF-8 -*-
'''Seção 03 - Exercício 6

    Faça um algoritmo que pergunte quanto você ganha
    por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.
'''
#Entrada
salarioHora = float(input("Digite o valor do seu salário por hora: "))
horasMes = float(input("Digite a quantidade de horas trabalhadas neste mês: "))

#Processamento
salarioTotal = salarioHora*horasMes

#Saída
print("O valor total do seu sálario para este mês é: R$ {0}".format(salarioTotal))