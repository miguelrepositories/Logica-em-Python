#-*- coding: UTF-8 -*-
'''Seção 08 - Exercício 3

    Faça um programa que carregue um vetor com dez números
    inteiros. Mostre o vetor na ordem inversa a que foi digitado.
'''
#Variáveis
vet1 = []
vet2 = []

#Entradas
print("Informe a seguir dez números inteiros.")
for i in range(10):
    vet1.append(int(input("Digite o {0}º número: ".format(i+1))))

#Processamento/Saída
for i in range(9, -1, -1): #Nesta parte também poderia ser usado a função .reverse()
    print("Vetor1[{0}] = {1}".format(i, vet1[i]))

    