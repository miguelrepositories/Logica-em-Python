#-*- coding: UTF-8 -*-
'''Seção 07 - Exercício 3

  Construa um algoritmo que leia 10 valores inteiros e positivos e:
  a) Encontre o maior valor
  b) Encontre o menor valor
  c) Calcule a média dos números lidos
'''
#Variáveis
maior = 0
menor = 99999*99999
soma = 0

#Entrada/Processamento
print("Digite a seguir 10 valores inteiros e positivos.")
for n in range(1, 11):
    valor = int(input("Informe um valor: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input("Informe um valor: "))
media = soma / 10
#Saídas
print("\na) O maior valor digitado foi: {0}".format(maior))
print("b) O menor valor digitado foi: {0}".format(menor))
print("c) A média dos valores é: {0:.2f}".format(media))
