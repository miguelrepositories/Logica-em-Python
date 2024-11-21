#-*- coding: UTF-8 -*-
'''Seção 07 - Exercício 3
    
    Faça um programa que leia um nome de usuário e a sua senha e não
    aceite a senha igual ao nome do usuário, monstrando uma mensagem
    de erro e voltando a pedir as informações.
'''

#Entrada
usuario = str(input("Usuário: "))
senha = str(input("Senha: "))

#Processamentos
while usuario == senha:
    print("O seu nome de usuário deve ser diferente da sua senha.")
    usuario = str(input("\nUsuário: "))
    senha = str(input("Senha: "))

