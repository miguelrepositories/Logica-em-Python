#-*- coding: UTF-8 -*-
'''Seção 07 - Exercício 7

    Sua organização acaba de contratar um estagiário para trabalhar no
    Suporte de Informática, com a intenção de fazer um levantamento
    nas sucatas encontradas nesta área. A primeira tarefa dele é testar
    todos os cerca de 200 mouses que se encontram lá, testando e anotando o
    estado de cada um deles, para verificar o que se pode aproveitar deles.
    Foi requisitado que você desenvolva um programa para registrar este
    levantamento. O programa deverá receber um número indeterminado
    de entradas, cada uma contendo: um número de identificação do
    mouse o tipo de defeito:
    - necessita da esfera;
    - necessita de limpeza;
    - necessita troca do cabo ou conector;
    - quebrado ou inutilizado

    Uma identificação igual a zero encerra o programa. Ao final o
    programa deverá emitir o seguinte relatório:

    Quantidade de mouses: 100

    Situação                                Quantidade    Percentual
    1- Necessita da esfera                    40            40%
    2- Necessita de limpeza                   30            30%
    3- Necessita troca do cabo ou conector    15            15%
    4- Quebrado ou inutlizado                 15            15%
'''
#Variáveis
defeito = 0
esfera = 0
limpeza = 0 
cabo = 0
quebrado = 0
cod = None

#Entradas
while cod != 0:
    cod = int(input("\nDigite por gentileza o código do mouse: "))
    if cod == 0:
        break
    print("Identifique o problema: ")
    print("1- Necessita da esfera ")
    print("2- Necessita de limpeza ")
    print("3- Necessita troca do cabo ou conector ")
    print("4- Quebrado ou inutilizado ")
    defeito = int(input("Digite o número do problema: "))

    #Processamentos
    if defeito == 1:
        esfera += 1
    elif defeito == 2:
        limpeza += 1
    elif defeito == 3:
        cabo += 1
    elif defeito == 4:
        quebrado += 1

qtde = esfera+limpeza+cabo+quebrado
percent1 = esfera / qtde * 100.0
percent2 = limpeza / qtde * 100.0
percent3 = cabo / qtde * 100.0
percent4 = quebrado / qtde * 100.0

#Saídas
print("\nQuantidade de mouses: {0}\n".format(qtde))
print("Situação                           Quantidade  Percentual");
print("1- Necessita da esfera                  {0}        {1:.2f}%".format(esfera, percent1))
print("2- Necessita de limpeza                 {0}        {1:.2f}%".format(limpeza, percent2))
print("3- Necessita troca do cabo ou conector  {0}        {1:.2f}%".format(cabo, percent3))
print("4- Quebrado ou inutilizado              {0}        {1:.2f}%".format(quebrado, percent4))