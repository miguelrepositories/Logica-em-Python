#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 10

   Elabore um algoritmo que dada a idade de um nadador classifique-o em
   uma das seguintes categorias:
   infantil-a = 5 a 7 anos
   infantil-b = 8 a 11 anos
   juvenil-a = 12 a 13 anos
   juvenil-b = 14 a 17 anos
   adultos = Maiores de 18 anos
'''
#Entrada
idade = int(input("Informe a idade do nadador: "))

#Processamentos
if idade < 5:
    #Saída
    print("Este nadador não possui idade suficiente.")
elif idade >=5 and idade <= 7:
    #Saída
    print("Este nadador pertence a categoria 'infantil-a'.")
elif idade >= 8 and idade <= 11:
    #Saída
    print("Este nadador pertence a categoria 'infantil-b'.")
elif idade >= 12 and idade <= 13:
    #Saída
    print("Este nadador pertence a categoria 'juvenil-a'.")
elif idade >= 14 and idade <= 17:
    #Saída
    print("Este nadador pertence a categoria 'juvenil-b'.")
elif idade >= 18:
    #Saída
    print("Este nadador pertence a categoria 'adultos'.")