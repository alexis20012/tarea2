# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:04:18 2020

@author: ALEXIS20012
"""
import random 
import pyautogui as pg
print(pg.position())
print("para que la maguia funcione asegurese de tener phyton y chrome abierto y python en una esquinita")
print("bienveniado a el mejor contador de chistes")
n=str(input("que categoria desea ingresar\n1.deportes de apreciación \n2.clavados \n3.patinaje artístico \n4.gimnasia \n5.entre más mejor la broma\n\n\n▲advertencia no coloque otro numero▲\n"))

if n==1:
    pg.click(416,48)
    pg.typewrite("https://www.youtube.com/channel/UC4ZOUyoqYbZaMl4lszAtr1Q")
    pg.typewrite(["enter"])
    pg.moveTo(random.randrange(0,1365),random.randrange(0,7604),5)
elif n==2:
    pg.click(416,48)
    pg.typewrite("http://verikosesi.rf.gd/pages/aula/progravanzada/inicio3.html")
    pg.typewrite(["enter"])
    pg.moveTo(random.randrange(0,1365),random.randrange(0,7604),5)
elif n==3:
    pg.click(416,48)
    pg.typewrite("https://dictionary.cambridge.org/es/translate/")
    pg.typewrite(["enter"])
    pg.moveTo(random.randrange(0,1365),random.randrange(0,7604),5)
elif n==4:
    pg.click(416,48)
    pg.typewrite("https://pythones.net/funciones-predefinidas-crear-nuestra-funcion/")
    pg.typewrite(["enter"])
    pg.moveTo(random.randrange(0,1365),random.randrange(0,7604),5)

elif n==5:
    pg.click(416,48)
    pg.typewrite("https://www.antena3.com/liopardo/memes/chistes-cortos-que-haran-llorar-risa-instante_201905105cd5aa820cf26b6ffc6a0941.html")
    pg.typewrite(["enter"])
    pg.moveTo(random.randrange(0,1365),random.randrange(0,7604),5)
else:
            
    web=["https://www.w3schools.com/python/ref_string_format.asp","https://canvas.instructure.com/",
         "https://www.lasexta.com/noticias/se-habla/mejores-chistes_202008035f2821076cf6da000167ab56.html",
         "https://www.nationalgeographic.es/","https://support.microsoft.com/es-es/windows/configuraci%C3%B3n-de-inicio-de-windows-incluyendo-el-modo-seguro-7f31dcea-6427-0ba0-ec1b-729a56321cd3",
         "https://www.anaconda.com/products/individual","https://es.liveworksheets.com/worksheets/en/English_as_a_Second_Language_(ESL)/Physical_description/Physical_Appearance_fh606074my",
         "https://www.epicgames.com/store/es-MX/","https://es.duolingo.com/","https://github.com/","https://elcodigoascii.com.ar/"]  
    pg.click(416,48)
    r=random.randrange(0,12)
    pg.typewrite(web[r])
    pg.typewrite(["enter"])
    pg.moveTo(random.randrange(0,1365),random.randrange(0,7604),10)
    
    pg.click(416,48)
    r=random.randrange(0,11)
    pg.typewrite(web[r])
    pg.typewrite(["enter"])
    pg.moveTo(random.randrange(0,1365),random.randrange(0,7604),10)
    
    
    
    