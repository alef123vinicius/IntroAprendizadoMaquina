#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 07:23:35 2018

@author: alef

K-NN

Passos para implementar o K-nn
1 - Preparar o conjunto de dados (entrada e saida)
2 - Informar o valor de K
3 - Para cada amostra 
    a - calcular a distancia euclidiana para todas as amostras
    b - determinar o conjunto das k distancias mais proximas
    c - o rótulos com mais representantes no conjunto dos K's será escolhido
4 - retornar o conjunto de rotulos de classificação
"""
import math as m
import matplotlib.pyplot as plt
import csv 
import random

def aleatorio(data):
    result = []
    while len(result) != len(data):
        r = random.randint(0, len(data)-1)
        if r not in result:
            result.append(r)
    new_d = []
    for i in range(len(result)):
        new_d.append(data[result[i]])
    
    return new_d

def distancia_euclidiana(c_t,n_i):
    """
    dist = Raiz ((X-x1)^2  + (Y - y1)^2 ... + (N - n1)^2)
    """
    vet_dist = []
    for j in range(len(c_t)):
        soma = 0
        for i in range(len(c_t[j])):
            soma = soma + (n_i[i] - c_t[j][i])**2
        vet_dist.append(m.sqrt(soma))
    return vet_dist
     
def predict(distancia, Y, classes, lista_k):
    cont_class = []
    for i in range(len(classes)):
        cont_i = 0
        for j in lista_k:
            if(Y[j] == classes[i]):
                cont_i = cont_i + 1
        cont_class.append(cont_i)
        
    return cont_class
        
def k_proximo(k, distancia):
    index = []
    compare = []
    for i in range(len(distancia)):
        compare.append(distancia[i])
        index.append(i)
    lista_index = []
    for i in range(len(compare)):
        lista_index.append(index[compare.index(min(compare))])
        index.remove(index[compare.index(min(compare))])
        compare.remove(min(compare))
        if(i == k-1 ):
            break
        
    return lista_index
  
def main():  
    with open('iris.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro)
        data = []
        for linha in reader:
            data.append(linha)
    #print(data)
    data = aleatorio(data)
    #Passo 1
    c_treinamento = []
    c_saida_rotulada = []
    for i in range(len(data)):
        vet = []
        for j in range(len(data[i])-2):
            vet.append(float(data[i][j]))
        c_treinamento.append(vet)
        c_saida_rotulada.append(data[i][4])
    
    #c_treinamento = [[1,1],[3,3],[5,5],[6,6],[4,4],[1,2]]
    #c_saida_rotulada = [1,1,0,0,0,1]
    novas_instancias = c_treinamento[25:len(c_treinamento)-1]
    saida_instancias = c_saida_rotulada[25:len(c_saida_rotulada)-1]
    classes = ['Iris-setosa','Iris-versicolor','Iris-virginica']
    #Passo 2 escolher um K (pode-se utilizar um algoritmo de otimização)
    k = 1
    acertos = 0
    for i in range(len(novas_instancias)):
        #Passo 3 - a - calcular as distâncias
        distancia = distancia_euclidiana(c_treinamento[0:24],novas_instancias[i])
        #print("distancias calculadas: ",distancia)
        
        #Passo 3 - b - determinar o conjunto k das distancias mais proximas
        lista_k = k_proximo(k,distancia)
        #print("lista dos k escolhidos: ",lista_k)
        #Passo 3 - c - votação 
        cont_class = predict(distancia, c_saida_rotulada[0:24], classes, lista_k)
        print("resultado da votacao: ",cont_class,"interacao: ",i)
        
        resp = cont_class.index(max(cont_class))
        print("entrada: ",novas_instancias[i], "saida: ",saida_instancias[i], "result:",classes[resp])
        
        if(classes[resp]  == classes[0]):
            plt.plot(novas_instancias[i][0],novas_instancias[i][1], 'b^')
            if(classes[resp]==saida_instancias[i]):
                acertos = acertos + 1
        if(classes[resp]  == classes[1]):
            plt.plot(novas_instancias[i][0],novas_instancias[i][1], 'r^')
            if(classes[resp] == saida_instancias[i]):
                acertos = acertos + 1
        if(classes[resp]  == classes[2]):
            plt.plot(novas_instancias[i][0],novas_instancias[i][1], 'g^')
            if(classes[resp] == saida_instancias[i]):
                acertos = acertos + 1
        #plt.plot(novas_instancias[i][0],novas_instancias[i][1],'yo')
    
    for i in range(len(c_saida_rotulada)):
        if(c_saida_rotulada[i]  == classes[0]):
            plt.plot(c_treinamento[i][0],c_treinamento[i][1], 'bo')
        if(c_saida_rotulada[i]  == classes[1]):
            plt.plot(c_treinamento[i][0],c_treinamento[i][1], 'ro')
        if(c_saida_rotulada[i]  == classes[2]):
            plt.plot(c_treinamento[i][0],c_treinamento[i][1], 'go')
       
    plt.xlabel("X")
    plt.ylabel("Y")
    #plt.axis(0,6,0,6)
    plt.show()
    
    
    print("total de acertos: ",acertos)
    print("total verificado: ",len(c_saida_rotulada[25:len(c_treinamento)]))
    
    
    
    
    
if __name__ == "__main__":
    main()