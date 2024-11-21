#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 6

    Elabore um algoritmo que leia as variáveis 'c' e 'n', respectivamente código
    e número de horas trabalhadas de um operário. Calcule o salário sabendo-se
    que ele ganha R$ 10,00 por hora. Quando o número de horas exceder a 50 calcule
    o excesso de pagamento armazenando-o na variável 'e'. Caso contrário zerar
    tal variável. A hora excedente de trabalho vale R$ 20,00. No final do 
    processamento imprimir o salário total e o salário excedente.
'''
#Entradas
c = int(input("Digite o código do operário: "))
n = float(input("Digite o total de horas trabalhadas: "))

#Processamento
if n > 50.00:
    e = (n-50.00)*20.00
    salarioTotal = (50.00*10.00) + e
else:
    e = 0 
    salarioTotal = 0

#Saída
print("Salário Excedente: R$ {0:.2f}\nSalário Total: R$ {1:.2f}".format(e, salarioTotal))