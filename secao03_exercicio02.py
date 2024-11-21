#-*- coding: UTF-8 -*-
''' Seção 03 - Exercício 2

    Faça um algoritmo para "calcular o estoque médio de uma peça",
    sendo que:
    
    estoque_medio = (quantidade_mínima + quantidade_maxima) / 2
'''

#Entrada
qtdeMax = int(input("Digite a quantidade máxima: "))
qtdeMin = int(input("Digite a quantidade mínima: "))

#Processamento
estoqueMedio = (qtdeMax + qtdeMin) / 2

#Saída
print("\nO estoque médio desta peça é: {0}".format(estoqueMedio))