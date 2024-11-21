#-*- coding: UTF-8 -*-
'''Seção 08 - Exercício 5

   Faça um programa que carregue um vetor com dez números inteiros.
   Calcule e mostre os números superiores a 50 e suas respectivas posições.
   Mostrar mensagem se não existir nenhum número nesta condição.
'''
#Variáveis
vet = []
boolean = False

#Entradas
print("Digite a seguir dez números inteiros.")
for i in range(10):
    vet.append(int(input("Informe o {0}º número: ".format(i+1))))
for i in range(10):
    if vet[i] > 50:
        print("Vetor[{0}] = {1}".format(i, vet[i]))
        boolean = True
if boolean == False:
    print("\nO vetor não possui nenhum elemento maior que 50.")