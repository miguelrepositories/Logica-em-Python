#-*- coding: UTF-8 -*-
'''Seção 08 - Exercício 6

   Faça um programa que receba um código númerico inteiro e um
   vetor de cinco posições de números reais. Se o código for zero,
   termine o programa. Se o código for 1, mostre o vetor na ordem
   direta. Se o código for 2, mostre o vetor na ordem inversa.
'''
import  sys
#Variáveis
cod = 0
vet = []

#Entradas
for i in range(5):
    vet.append(float(input("Digite um valor para {0}/5: ".format(i+1))))

#Processamentos    
print("\nEscolha uma das opções a baixo:");
print("1- Mostrar o vetor na ordem direta");
print("2- Mostrar o vetor na ordem inversa");
print("0- Sair");
cod = int(input("Digite sua escolha: "))

if cod == 1:
    for i in range(5):
        print("{0:.2f} ".format(vet[i]))
    sys.exit()
if cod == 2:
    vet.reverse()
    for i in range(5):
        print("{0:.2f} ".format(vet[i]))
    sys.exit()
if cod == 0:
    print("\nAplicação encerrada...")
    sys.exit()
    
        