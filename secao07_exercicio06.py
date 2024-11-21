#-*- coding: UTF-8 -*-
'''Seção 07 - Exercício 6

   Desenvolva um gerador de tabuada, capaz de gerar a tabuada de
   qualquer número inteiro entre 1 a 10. O usuário deve informar
   de qual número ele deseja ver a tabuada. A saída deve ser
   conforme o exemplo abaixo:
   
   Tabuada de 5:
   5 x 1 = 5
   5 x 2 = 10
   ...
   5 x 10 = 50
'''
#Entrada
print("A seguir, digite um número de 1 a 10, para que seja apresentada a tabuada.")
num = int(input("Digite o número: "))

#Processamento/Saída
print("\nTabuada de {0}: ".format(num))
for i in range(1, 11):
    print("{0} x {1} = {2}".format(num, i, num*i))    