# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:59:29 2020

@author: ALEXIS20012
"""

class banco():
    print("BIENVENIDO A ADFE")
    numero_cuenta=int(input("ingrese su numero de cuenta:"))
    nombre=str(input("ingrese su nombre:"))
    ingreso=float(input("ingrese su balance general:"))
    ban=(str(input("ingrese el nombre del banco:"))).upper()
    metodop="*"
    tarjeta=0
    ingrese=0
    cambio=0
    def impuesto(self):
        if(self.ban=="ADFE"):
            imp=0
        else:
            imp=0.05
        self.ingreso=round(self.ingreso+(self.ingreso*imp))
        
        print("el monto total es de $"+str(self.ingreso)+"MX")
        #return ingreso
    def deposito(self):
        self.metodop=str(input("como quiere realizar su pago:\n1.tarjeta\n2.efectivo\n"))
        if(self.metodop=="tarjeta" or self.metodop=="1"):
            self.tarjeta=int(input("ingrese el numero de tarjeta:"))
            self.metodop="tarjeta"
        else:
            self.ingrese=float(input("ingrese el monto $"))
            self.cambio=self.ingrese-self.ingreso
            self.metodop="efectivo"
       ### return ingrese,cambio,metodop
    def metodo(self):
        d=int(input("sea mostar el nombre\n 1.si 0.no:"))
        p=int(input("sea mostar el numero de cuenta\n 1.si 0.no:"))
        g=int(input("sea mostar su metodo de pago\n 1.si 0.no:"))
        k=int(input("sea mostar el numero de cuenta a pagar\n 1.si 0.no:"))
        t=int(input("sea mostar el ingreso\n 1.si 0.no:"))
        r=int(input("sea mostar la cantidad que deposito\n 1.si 0.no:"))
        f=int(input("sea mostar el cambio\n 1.si 0.no:"))
        print(d*("\nseñor o señora:"+self.nombre)+p*("\nnumero de cuenta:"+str(self.numero_cuenta)))
        print(g*("metodo de pago:"+self.metodop)+k*("\nnumero de cuenta:"+str(self.tarjeta))+t*("\nun monto de $"+str(self.ingreso)))
        print(r*("cantidad que deposito $"+str(self.ingrese))+f*("\ncambio$"+str(self.cambio)))
usuario=banco()
usuario.impuesto()
usuario.deposito()
usuario.metodo()