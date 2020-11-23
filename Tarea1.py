# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:40:00 2020

@author: ALEXIS20012
"""
import math
class figura():
    
    altura=0
    base=0
    base2=0
    radio=0
    piezas=0
    def perimetrog(self):
        perimetro_general=(2*self.base2)+(2*self.base)
        return "el perimetro es",perimetro_general
    def perimetro2(self):
        perimetro_p=self.base*self.piezas
        return "el perimetro es",perimetro_p
    
    def triangulo(self):
        perimetro_triangulo=self.base2+self.base+self.piezas
        self.s=(perimetro_triangulo)/2
        Area_triangulo=round(math.sqrt((self.s*(self.s-self.base2)*(self.s-self.base)*(self.s-self.piezas))))
        return "el perimetro es",perimetro_triangulo,"\n el area es",Area_triangulo
    def circulo(self):
        perimetro_circulo=math.pi*self.radio*2
        Area_circulo=math.pi*pow(self.radio,2)
        return "el perimetro del circulo es",perimetro_circulo," \nel area del circulo es:",Area_circulo
    def poligono(self):
        perimetro_poligono=self.piezas*self.base
        Area_poligono=(perimetro_poligono)*self.altura/2       
        return "el perimetro es:",perimetro_poligono,"\n el area es:",Area_poligono
    def cuadrado(self):
        Area_cuadrado=pow(self.base,2)
        return "el area es",Area_cuadrado
    def rectangulo(self):
        Area_rectangulo=self.base*self.base2
        return "el area es",Area_rectangulo
    def rombo(self):
        Area_rombo=(self.base2*self.altura)/2
        return "el area es:",Area_rombo
    def trapesio(self):
        perimetro_trapesio=self.base2+self.base+self.radio+self.piezas
        h=math.sqrt((pow(self.base-self.base2,2)+pow(self.radio, 2)))
        Area_trapesio=((self.base+self.radio)/2)*h
        return "el perimetro es:",perimetro_trapesio,"\n el area es:",Area_trapesio
    
    def paralegramo(self):
        Area_paralelogramo=self.base*self.altura
        return "el area es",Area_paralelogramo
        
def entrada_de_datos():
    figuras.base=float(input("ingrese el valor de la base x="))
    figuras.base2=float(input("ingrese el valor de la altura y="))    
x=0
y=0
menu=1

while(menu>0):
    figuras=figura()
    menu=int(input("contamos con:\n______________\n1.cuadrado\n2.rectangulo\n3.triangulo\n4.rombo\n5.paralelogramo\n6.trapecio\n7.poligono\n8.circulo\n_____________\n9.salir\n10.intrucciones\n[que opcion elige]:"))
    if(menu==1):
        print("ingreso al cuadrado ▀")
        figuras.piezas=4
        figuras.base=float(input("ingrese el volor de la base x="))
        
        print(figuras.perimetro2())
        print(figuras.cuadrado()) 
    elif(menu==2):
        print("ingreso al rectangulo █")
        entrada_de_datos()
        print(figuras.perimetrog())
        print(figuras.rectangulo()) 
    elif(menu==3):
        print("ingreso al triangulo ▲")
        figuras.piezas=float(input("ingrese el valor de la hipotenusa="))
        entrada_de_datos()
        print(figuras.triangulo())
    elif(menu==4):
        print("ingreso al rombo ♦")
        figuras.piezas=4
        print("ingrese el tamaño de y el ancho")
        entrada_de_datos()
        figuras.altura=float(input("ingrese la altura del rombo:"))
        print(figuras.perimetro2())
        print(figuras.rombo())
    elif(menu==5):
        print("ingreso al paralelogramo ♠")
        figuras.altura=float(input("ingrese la altura de su palalelogramo="))
        entrada_de_datos()
        print(figuras.perimetrog())
        print(figuras.paralegramo())
    elif(menu==6):
        print("ingreso al trapecio ♣")
        entrada_de_datos()
        figuras.radio=float(input("ingrese el volor de la base x'="))
        figuras.pieza=float(input("ingrese el valor de la altura y'="))
        print(figuras.trapesio())
    elif(menu==7):
        print("ingreso al poligono ♥")
        figuras.base=float(input("ingrese el tamaño del poligono="))
        figuras.piezas=float(input("cuantos piezas desea="))
        figuras.altura=(float(input("ingrese el tamaño del la altura'=")))
        print(figuras.poligono())
    elif(menu==8):
        print("ingreso al circulo ○")
        figuras.radio=float(input("ingrese el radio="))
        print(figuras.circulo())
    elif(menu==9):
        menu=str(input("♠esta segura de que quieres salir♠\n\t[si]\t[no]\n"))
        if menu=="si":
            menu=0
        else:
            menu=1
    elif(menu==10):
        print("este te menti jajajajajajaja")
    else:
        print("\n|error no se encontro el valor deseado, vuelva a intentar|\n")

print("♥ gracias por usar mi APP que me costo hacerlo =) ♥")
