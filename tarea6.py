# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 23:11:05 2020

@author: ALEXIS20012
"""
import sympy as sp
def poli (entrada,xa):
    y=sp.sympify(entrada)
    f=y.evalf(subs={x:xa})
    return(f)
    
no=str(input("1.limpiar el texto:\n1.si\t2.no\n"))
if(no=="1" or no=="si"):
    bug=open("metodobi.txt","w")
else:
    bug=open("metodobi.txt","a")

x=sp.Symbol('x')
ecuacion=input("ingrese una ecuacion:")
y=sp.sympify(ecuacion)
print(sp.pretty(y))
sp.plotting.plot(y, xlabel = 'x', ylabel = 'y')

print("calculadora de raiz por el metodo de Bisección")
xi=float(input("ingrese el valor de xi="))
xs=float(input("ingrese el valor de xs="))
error=float(input("ingrese el valor de el error="))
xa=(xi+xs)/2.0

i=0
signo="negativo"
limite="superior"
print("{:^13}{:^13}{:^13}{:^13}{:^13}{:^13}{:^13}".format("i","xi","xs","xa","signo","cambio","error"))
texto=str("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("i","xi","xs","xa","signo","cambio","error"))
bug.write(texto)
bug.write("\n")
while abs(poli(y,xa)) > error :
    i+=1
    xa=(xi+xs)/2.0
    print("{:^12}{:^12.4f}{:^12.4f}{:^12.4f}{:^12}{:^12}{:^12.4f}".format(i,float(xi),float(xs),float(xa),signo,limite,float(poli(y,xa))))
    texto=str("{:^12}{:^10.4f}{:^10.4f}{:^10.4f}{:^10}{:^10}{:^10.4f}".format(i,float(xi),float(xs),float(xa),signo,limite,float(poli(y,xa))))
    bug.write(texto)
    bug.write("\n")
    if (poli(y,xi)*poli(y,xa)) < 0:
        xs=xa
        signo="negativo"
        limite="superior"
    else:
        poli(y,xi)
        xi=xa
        signo="positivo"
        limite="inferior"
    if(xi==xa):
        print("la raiz es imaginaria o no es calculabre")
        break
    
print("la raiz es",xa)

texto=("la raiz es:"+str(xa))
bug.write(texto)
bug.write("\n")
bug.close()