#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:03:08 2018

@author: alef

Perceptron pseudo codigo

1 - iniciar os pesos sinápticos com valores randomicos e pequenos ou iguais a zero wij ;
2 - aplicar um padrão com seu respectivo valor desejado de saída (tj) e verificar a saida da rede (sj);
3 - calcula o erro na saída Ej = tj - sj;
4 - se Ej = 0, volta ao passo 2;
    se Ej != 0, atualiza os pesos: delta wij = n * xi * Ej

5 - volta ao passo 2.

se a saida estiver correta não ocorre  variação
caso contrario
    o peso é incrementado de n quando a saida é menor que o target
    o peso é decrementado de n quando a saida é maior que o target
    
    delta wij = n * xi * Ej

"""
import matplotlib.pyplot as plt
import random

def somatorio(X,w,bias):
    soma = 0
    for i in range(len(X)):
        soma = soma + X[i]*w[i]
    
    return soma + bias

def fnet(net):
    if(net > 0):
        return 1
    else:
        return 0
def aleatorio(X):
    w = []
    for i in range(len(X[0])):
        w.append(random.uniform(0,1))
    return w

def main():
    X = [[1,1],[2,2],[5,5],[6,6],[4,4],[1,2]]
    Y = [1,1,0,0,0,1]    
    nX = [[0,1],[1,3],[4,5],[3,4]]
    nY = [1,1,0,0]
    classes = [0,1]
    
    #1 - definir os pesos da rede 
    w = aleatorio(X)
    print(w)
    #definir a taxa de aprendizado N e o bias (deslocar o hiperplano)
    n = 0.2
    bias = 0.5
    erro_total = 2
    epoca = 11
    interacao = 0
    geracao = 0
    #etapa de treinamento 
    #-------------------------------------------------------------------------------------------
    while(erro_total >0 and interacao < epoca):
        erro_total = 0
        for i in range(len(X)):
        #2 - calcular o somatorio e encontrar a f de net ou seja encontrar o Y de saida
            net = somatorio(X[i],w,bias)
            
            S = fnet(net)
            #3 - calcular o erro da saida
            erro = Y[i] - S
            
            #4 - verificação de erro
            if(erro != 0):
                erro_total = erro_total + 1
                for j in range(len(w)):
                    if(S > Y[j]):
                        w[j] = w[j] - n*X[i][j]*erro
                    else:
                        w[j] = w[j] + n*X[i][j]*erro
            print("_____________________________________________________________")
            print("| entrada: ",X[i],"saida calc/esperada: ", S,Y[i],"erro: ",erro)
            print("| pesos: ",w)
            print("| interacao:", interacao)
        interacao = interacao + 1
        if(interacao == epoca and erro_total> 0):
            w = aleatorio(X)
            interacao = 0
            geracao = geracao + 1
            
    #maximo onze epocas e tem-se uma geração nova de pesos
    print("Geracao: ",geracao, "epoca: ",interacao)
    
    #--------------------------------------------------------------------------------------------------
    #etapa de teste
    erro_total = 0
    for i in range(len(nX)):
        net = somatorio(nX[i],w,bias)
        S = fnet(net)
        erro = nY[i] - S
        if(erro != 0):
            erro_total = erro_total + 1
            if(S == classes[0]):
               plt.plot(nX[i][0],nX[i][1], 'bx') 
            else:
               plt.plot(nX[i][0],nX[i][1], 'rx') 
        else:
           if(S == classes[0]):
               plt.plot(nX[i][0],nX[i][1], 'b^') 
           else:
               plt.plot(nX[i][0],nX[i][1], 'r^') 
            
        print("_____________________________________________________________")
        print("| entrada: ",nX[i],"saida calc/esperada: ", S,nY[i],"erro: ",erro)
    
    
        
    
    for i in range(len(Y)):
        if(Y[i]  == classes[0]):
            plt.plot(X[i][0],X[i][1], 'bo')
        if(Y[i]  == classes[1]):
            plt.plot(X[i][0],X[i][1], 'ro')
    
    plt.xlabel("param1")
    plt.ylabel("param2")
    plt.show()
    

if __name__ == "__main__":
    main()