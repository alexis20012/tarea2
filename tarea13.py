# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:16:04 2020

@author: ALEXIS20012
"""
import re
t=open("poema.txt","r")
texto=t.read()
letra_minisculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t",
                  "u","v","w","x","y","z"]
letra_mayuscula=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T",
                  "U","V","W","X","Y","Z"]
numeros=["0","1","2","3","4","5","6","7","8","9"]
print("el total de letras son:\n")
l=0
for tmp in range(0,len(letra_mayuscula),1):
    x=len(re.findall(letra_mayuscula[tmp],texto))
    y=len(re.findall(letra_minisculas[tmp],texto))
    print("hay un total de",letra_mayuscula[tmp]+":",str(x))
    print("hay un total de",letra_minisculas[tmp]+":",str(y))
    l=l+x+y
print("\nson {} palabras".format(l))
print("\nel numero de letras son:\n")
for tmp in range(0,len(numeros),1):
    n=len(re.findall(numeros[tmp],texto))
    print("hay un total de",numeros[tmp]+":",str(n))
    l=n+l
print("\nson {} numeros".format(l))
n=len(re.findall(" ",texto))
print("\ntotal de espacios:",str(n))
print("gracias por esar mi app :)")
t.close()