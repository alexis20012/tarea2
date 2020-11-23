# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:46:13 2020

@author: ALEXIS20012
"""
import sympy as sp
print(" Método de Lin-Bairstow")
no=str(input("1.limpiar el texto:\n1.si\t2.no\n"))
if(no=="1" or no=="si"):
    bug=open(" Método de Lin-Bairstow.txt","w")
else:
    bug=open(" Método de Lin-Bairstow.txt","a")
x = sp.Symbol('x')
ecuacion=str(input("ingrese la ecuacion:"))
y=sp.simplify(ecuacion)
print(sp.pretty(y))
sp.plotting.plot(y)
r=float(input("ingrese el valor inicial de r:"))
s=float(input("ingrese el valor inicial de s:"))
error=float(input("ingrese el valor del error:"))
a=[]
b=[]
c=[]
p=y
h=float(p.evalf(subs={x:0}))
a.append(h)
i=0
#factorizador =)
for tmp in range(0,len(ecuacion),1):
    
    p=(p-a[i])
    p=sp.simplify(p/x)
    h=float(p.evalf(subs={x:0}))
    if(p==0):
        break
    if(h==0):
        a.append(h)
        i+=1  
    else:
        a.append(h)
        i+=1 
es=0
n=1
print("{:^12}{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}".format("n","dr","ds","r","s","%error.r","error.s"))
texto=("{:^12}{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}".format("n","dr","ds","r","s","%error.r","error.s"))
bug.write(texto)
bug.write("\n")
while (es>=0):
    l=len(a)-1
    b.append(a[l])   
    b.append(a[l]+r*b[0])   
    i=-1
    for tmp in range(l-2,-1,-1): 
        
        if i==len(a)-3:
            break
        p=a[tmp]+r*b[i+1]+s*b[i+2]
        b.append(p)
        i+=1
       # print(tmp)
    l=len(b)-1
    c.append(b[l])   
    c.append(b[l]+r*c[0])   
    i=-1
    for tmp in range(l-2,-1,-1): 
        
        if i==len(b)-4:
            break
        p=b[tmp]+r*c[i+1]+s*c[i+2]
        c.append(p)
        i+=1    
    b.reverse()
    c.reverse()
    dr=((c[2]-b[0])-(c[1]*b[1]))/((c[1]**2)-(c[0]*c[2]))
    ds=((c[0]*b[1])-(c[1]*b[0]))/((c[1]**2)-(c[0]*c[2]))
    r=r+dr
    s=s+ds
    
    er=(dr/r)*100
    if(er<0):
        er=er*-1
    es=(ds/s)*100
    if(es<0):
        es=es*-1
    print("{:^12}{:^20.6f}{:^20.6f}{:^20.6f}{:^20.6f}{:^20.6f}{:^20.6f}".format(n,float(dr),float(ds),float(r),float(s),float(er),float(es)))
    texto=("{:^12}{:^20.6f}{:^20.6f}{:^20.6f}{:^20.6f}{:^20.6f}{:^20.6f}".format(n,float(dr),float(ds),float(r),float(s),float(er),float(es)))
    bug.write(texto)
    bug.write("\n")
    n+=1
   
    if(er<=error):
        break
    
bug.close()
    