#-*- coding: UTF-8 -*-
'''Seção 06 - Exercicio 5

  João da Silva, pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
  Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado
  de São Paulo (50 Kg) deve pagar uma multa de R$ 4,00 por Kg excedente. João precisa que você faça um
  algoritmo que leia a variável 'p' (peso de peixes) e verifique se há excesso. Se houver gravar na
  variável 'e' (excesso) e na variável 'm' o valor da multa que João deverá pagar. Caso contrário mostrar
  tais variáveis com o conteúdo 'zero'.
'''

#Entrada
p = float(input("Digite o peso (Kg) de peixes que foram pescados: "))

#Processamentos
if p > 50:
    e = p - 50
    m = e * 4
else:
    e = 0.00
    m = 0.00
    
#Saída
print("Você excedeu o peso de pesca autorizado em: {0:.2f} Kg".format(e))
print("O valor da multa a pagar é: R$ {0:.2f}".format(m))