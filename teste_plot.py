#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:20:25 2018

@author: alef
"""
import math as m
import matplotlib.pyplot as plt
import csv 
import random

def aleatorio_data(data):
    result = []
    while len(result) != len(data):
        r = random.randint(0, len(data)-1)
        if r not in result:
            result.append(r)
    new_d = []
    for i in range(len(result)):
        new_d.append(data[result[i]])
    
    return new_d

def main():

    with open('iris.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro)
        data = []
        for linha in reader:
            data.append(linha)
    #print(data)
    data = aleatorio_data(data[0:99])
    #Passo 1
    X = []
    Y = []
    for i in range(len(data)):
        vet = []
        for j in range(len(data[i])-2):
            vet.append(float(data[i][j]))
        X.append(vet)
        if(data[i][4] == 'Iris-setosa'):
            Y.append(0)
        if(data[i][4] == 'Iris-versicolor'):
            Y.append(1)
    
    for i in range(len(Y[0:len(Y)-1])):
        if(Y[i] == 0):
            plt.plot(X[i][0],X[i][1], 'bo')
        else:
            plt.plot(X[i][0],X[i][1], 'ro')
    
    plt.xlabel("param1")
    plt.ylabel("param2")
    plt.show()
    
    
if __name__ == "__main__":
    main()