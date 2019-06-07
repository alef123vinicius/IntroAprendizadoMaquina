#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:34:00 2018

@author: alef

sklearn

"""

from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
digits = datasets.load_digits()


#clf.fit(iris.data[:-1],iris.target[:-1])

#print(clf.predict(iris.data[-1:]))
