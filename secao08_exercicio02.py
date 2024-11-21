#-*- coding: UTF-8 -*-
'''Seção 08 - Exercício 2

   Escreva um algoritmo que leia dois vetores de 10 posições e faça a
   soma dos elementos de mesmo índice, colocando o resultado em um
   terceiro vetor. Mostre o vetor resultante.
'''
#Variáveis
vet1 = []
vet2 = []
vet3 = []

#Entradas
for i in range(10):
    vet1.append(float(input("Digite {0}º número para o primeiro vetor: ".format(i+1))))
for i in range(10):
    vet2.append(float(input("Digite {0}º número para o segundo vetor: ".format(i+1))))
print("")
for i in range(10):
    vet3.append(vet1[i]+vet2[i])
    print("Vetor1[{0}] + Vetor2[{1}] = {2}".format(i, i, vet3[i])) 
