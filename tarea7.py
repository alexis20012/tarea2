# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:19:30 2020

@author: ALEXIS20012
"""
import sympy as sp
print("calculadora por Método de Newton - Raphson")
def poli (entrada,xa):
    y=sp.sympify(entrada).evalf(subs={x:xa})
    return(y)
def deriva(entrada,xa):
    y=sp.sympify(entrada)
    d=y.evalf(subs={x:xa})
    return d
    
no=str(input("1.limpiar el texto:\n1.si\t2.no\n"))
if(no=="1" or no=="si"):
    bug=open("Método de Newton.txt","w")
else:
    bug=open("Método de Newton.txt","a")
    
x=sp.Symbol('x')
ecuacion=input("ingrese una ecuacion:")
y=sp.sympify(ecuacion)
print(sp.pretty(y))
sp.plotting.plot(y, xlabel = 'x', ylabel = 'y')


x=float(input("ingrese el valor de inicio:"))
errorf=float(input("ingrese la cantidad de error:"))
raiz=[]
raiz.insert(0,0)
i=0
error=1
print("{:^12}{:^14}{:^14}".format("i","xl","error"))

while abs(error)>errorf:
    xl=x-(poli(y,x)/deriva(y,x))
    raiz.append(xl)
    i+=1
    x=xl
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print("{:^12}{:12.2f}{:12.6f}".format(i,x,error))
    texto=("{:^12}{:12.2f}{:12.6f}".format(i,x,error))
    bug.write(texto)
    bug.write("\n")

bug.close()