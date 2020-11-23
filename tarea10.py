# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:04:42 2020

@author: ALEXIS20012
"""
import random as rd
import numpy as np
import sympy as sp
import math as mt
import matplotlib.pyplot as mp
def formula_x(le,r):
    l=sp.Symbol("l")
    a=sp.Symbol("a")
    x=sp.simplify("l*cos(a)").evalf(subs={l:le,a:r})
    return float(x)
def formula_y(le,r):
    l=sp.Symbol("l")
    a=sp.Symbol("a")
    y=sp.simplify("l*sin(a)").evalf(subs={l:le,a:r})  
    return float(y)
l=float(input("ingrese la longitud:"))
n=int(input("ingrese el numero de pasos:"))
xi=[]
yi=[]
d=[]
for tmp in range(0,n+1,1):
    r=rd.uniform(0,2*np.pi)
    xi.append(formula_x(l, r))
    yi.append(formula_y(l, r))
    d.append(mt.sqrt((pow(xi[tmp],2)+pow(yi[tmp],2))))  
mp.plot(xi, yi, "-", linewidth=3, color = (rd.uniform(.1,1),rd.uniform(.1,1), rd.uniform(.1,1)))
mp.title("Simulación del camino aleatorio")
mp.grid()
mp.show()
print("el distancia mas larga conseguida fue de:"+str(max(d)))
