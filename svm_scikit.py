#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:33:01 2018

@author: alef
"""

from sklearn import svm 


def porta_xor():
    X = [[0,0],[1,1],[0,1],[0.5,0]]
    y = [0,0,1,1]
    clf = svm.SVC(gamma='scale')
    clf.fit(X,y)
    #testar a rede com novas instacias
    print(clf.predict([[1,0]]))
    #verificar os vetores de suporte escolhido
    print(clf.support_vectors_)
    #indices dos vetores de suporte
    print(clf.support_)
    #quantidade de vetores para cada classe
    print(clf.n_support_)
    
def svm_multclass():
    X = [[0],[1],[2],[3]]
    Y = [0,1,2,3]
    clf = svm.SVC(gamma = 'scale', decision_function_shape= 'ovo')
    clf.fit(X,Y)
    dec = clf.decision_function([[1]])
    print(dec.shape[1])

def svm_linear():
    X = [[0],[1],[2],[3]]
    Y = [0,1,2,3]
    clf = svm.LinearSVC()
    clf.fit(X,Y)
    
    dec = clf.decision_function([[1]])
    print(dec.shape[1])

    print(clf.predict([[0.4]]))
    
    
def main():
    svm_linear()
    
    

if __name__ == "__main__":
    main()    