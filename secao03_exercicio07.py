#-*- coding: UTF-8 -*-
'''Seção 03 - Exercício 7
    
    Tendo como dados de entrada a altura de uma pessoa,
    construa um algoritmo que calcule seu peso ideal,
    usando a seguinte fórmula: (72. 7 * altura) - 58
'''
#Entrada
altura = float(input("Digite a medida da sua altura: "))

#Processamento
pesoIdeal = (72.7 * altura) - 58

#Saída
print("O seu peso ideal é: {0:.2f}".format(pesoIdeal))