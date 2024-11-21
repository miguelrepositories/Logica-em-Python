#-*- coding: UTF-8 -*-
'''Seção 08 - Exercício 4

   Escreva um algoritmo que leia e mostre um vetor de 20 elementos
   inteiros, em seguida, mostre a soma de todos os elementos.    
'''
#Variáveis
vetor1 = []
soma = 0

#Entrada
for i in range(20):
    vetor1.append(int(input("Digite o {0}º elemento do vetor: ".format(i+1))))
    soma += vetor1[i] #Nesta parte poderia também ser usada a função sum()
    
#Saída
print("\nA soma dos elementos do vetor, equivale a: {0}".format(soma))