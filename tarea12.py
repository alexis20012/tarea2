# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:08:18 2020

@author: ALEXIS20012
"""

class tabla():
    
    nombre_ele=int
    simbolo="como"
    numero_ato="01"
    masa_ato="0.1"
    radio_ato="0"
    estado="mexico"
    def nombre(self):
        self.nombre_ele=str(input("ingrese el nombre del elemento:"))
        return self.nombre_ele
    def simbo(self):
        self.simbolo=str(input("ingrese el simbolo del elemento:"))
        return self.simbolo
    def numero(self):
        self.numero_ato=str(input("ingrese el numero atomico:"))
        return self.numero_ato
    def masa(self):
        self.masa_ato=str(input("ingrese la masa atomica:"))
        return self.masa_ato
    def radio(self):
        self.radio_ato=str(input("ingrese radio atomico:"))
        return self.radio_ato
    def estados(self):
        self.estado=str(input("ingrese el estado del elemento:"))
        return self.estado

no=str(input("1.limpiar el texto:\n1.si\t2.no\n"))
if(no=="1" or no=="si"):
    bug=open("tabla de elementos.txt","w")
else:
    bug=open("tabla de elementos.txt","a")

bug.write("{:^13}{:^20}{:^20}{:^20}{:^20}{:^20}".format("nombre del elemento","simbolo","numero atomico","masa atomica","radio atomico","estado ordinario"))
n=int(input("ingrese el numero de elementos que desea ingresar:"))
p=tabla()
bug.write("\n")
for t in range(1,n+1,1):
    
    tex=("{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}".format(str(p.nombre()),str(p.simbo()),str(p.numero()),str(p.masa()),str(p.radio()),str(p.estados())))
    bug.write(tex)
    bug.write("\n")
    print("el numero es:"+str(t)+"\n")

bug.close()

no=str(input("desea imprimir el texto\n1.imprimir el texto:\n1.si\t2.no\n"))
if(no=="1" or no=="si"):
    bug=open("tabla de elementos.txt","r")
    print(bug.read())

bug.close()

