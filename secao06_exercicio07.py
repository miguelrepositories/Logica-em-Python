#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 7

   Desenvolva um algoritmo que:
   a) Leia 4 (quatro) números;
   b) Calcule o quadrado de cada um;
   c) Se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
   d) Caso contrário, imprima os valores lidos e seus respectivos quadrados.
'''
#Entrada
numeros = []
resultados = []
for i in range(4):
    numeros.append(float(input("Digite o {0}º número: ".format(i+1))))

#Processamento
for i in range(4):
    resultados.append(float(numeros[i]**2))
    
if resultados[2] >= 1000:
    #Saída
    print("\nO quadrado do terceiro número digitado equivale a: {0:.2f}".format(resultados[2]))
else:
    for i in range(4):
        #Saída
        print("\nO {0}º número digitado foi: {1:.2f}\nSeu quadrado é: {2:.2f}".format(i+1, numeros[i], resultados[i]))

