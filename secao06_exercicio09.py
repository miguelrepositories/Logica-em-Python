#-*- coding: UTF-8 -*-
'''Seção 06 - Exercício 9
   A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3
   grupos de indústrias que são altamente poluentes do meio ambiente. O índice de
   poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias
   do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4
   as industrias de 1º e 2º grupo são intimadas a suspenderem suas atividades, se o
   índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades.
   Faça um algoritmo que leia o índice de poluição medido e emita uma notificação
   adequada aos diferentes grupos de empresas.
'''
#Entrada
indice = float(input("Informe o índice de poluição medido: "))

#Processamento
if indice < 0.3:
    #Saída
    print("\nÍndice de poluição tolerável.")
if indice >= 0.3 and indice < 0.4:
    #Saída
    print("\nATENÇÃO: Empresas do 1º grupo, suspender atividades.")
if indice >= 0.4 and indice < 0.5:
    #Saída
    print("\nATENÇÃO: Empresas do 1º grupo e 2º grupo, suspender atividades.")
if indice >= 0.5:
    #Saída
    print("\nATENÇÃO: Empresas de todos os grupos, suspender atividades.")
    