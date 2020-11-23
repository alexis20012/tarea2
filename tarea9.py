# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:33:46 2020

@author: ALEXIS20012
"""
import sympy as sp
print("Método de Trapecios")
no=str(input("1.limpiar el texto:\n1.si\t2.no\n"))
if(no=="1" or no=="si"):
    bug=open("deriva.txt","w")
else:
    bug=open("deriva.txt","a")
x = sp.Symbol('x')
ecuacion=input("ingrese la funcion:")
f=sp.sympify(ecuacion)
sp.plotting.plot(f)
n = int(input("ingrese un valor de interacion:"))
a = float(input("ingrese un valor de inicio:"))
b =float(input("ingrese un valor de final:"))
sp.plotting.plot(f,xlim = [a,b], ylim = [-4,4])
xi = []
sumar = 0
print("{:^4}{:^12}{:^12}".format("i", "xi","sumador"))
texto=("{:^4}{:^12}{:^12}\n".format("i", "xi","sumador"))
bug.write(texto)
for i in range(1, n):
    xi.append( (i)*(b-a)/n )
    sumar += f.subs(x, (i)*(b-a)/n ).evalf()
    print("{:^4}{:^12.4f}{:^12.4f}".format(i,xi[i-1],float(sumar)))
    texto=("{:^4}{:^12.4f}{:^12.4f}\n".format(i,xi[i-1],float(sumar)))
    bug.write(texto)
Res = (b-a) * ( (f.subs(x,a).evalf() + 2*sumar + f.subs(x,b).evalf() )/(2*n) )
bug.write("\n")
print("Resultado:{:.6f}".format(Res))
texto="Resultado:{:.6f}\n".format(Res)
bug.write(texto)
print("Real:{:.6f}".format(sp.integrate(f,(x, a,b))))
texto=("Real:{:.6f}\n".format(sp.integrate(f,(x, a,b))))
bug.write(texto)
bug.close