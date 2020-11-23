# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:55:26 2020

@author: ALEXIS20012
"""

def Reinas(solucion,etapa,n):
	if etapa>=n:                             # si la etapa es mayor que n, entonces devolvemos falso
		return False
	#solucion.append(0)
	exito = False                            # inicializamos exito a False
	
	while True:
            if (solucion[etapa] < n):                       # si el valor de la columna para la fila es mayor o igual que n, entonces no seguimos incrementando, con esto evitamos indices fuera del array.
                solucion[etapa] = solucion[etapa] + 1       # incrementamos el valor de columna para la reina i-esima de la fila i-esima.

            if (Valido(solucion,etapa)):                    # si la reina i-esima de la fila i-esima de la columna j en la etapa k no entra en conflicto con otra reina, proseguimos.

                if etapa != n-1:                            # si aun no hemos acabado todas las etapas, procedemos a la siguiente etapa.
                    exito = Reinas(solucion, etapa+1,n)
                    if exito==False:                        # si del valor devuelto de Reinas tenemos falso, ponemos a 0 el valor de la etapa + 1 para asi descartar los nodos fracaso.
                        solucion[etapa+1] = 0

                else:
                    print (solucion)                          # si ya hemos acabado, imprimimos la disposicion de las fichas en el tablero y devolvemos True.
                    for x in range(n):
                        for i in range(n):
                            if solucion[x] == i+1:
                                print (" ♥ ",end=("")),
                            else:
                                print (" █ ",end=(""))

                        print ("\n")
                    exito = True
            if (solucion[etapa]==n or exito==True):         # si el valor de la columna j de la etapa k es igual a n o exito es igual a True, salimos del bucle y devolvemos exito.
                break
	return exito


def Valido(solucion,etapa):
	# Comprueba si el vector solucion construido hasta la etapa es 
	# prometedor, es decir, si la reina se puede situar en la columna de la etapa

	for i in range(etapa):
		if(solucion[i] == solucion[etapa]) or (ValAbs(solucion[i],solucion[etapa])==ValAbs(i,etapa)):
			return False

	return True

def ValAbs(x,y):
	if x>y:
		return x - y
	else:
		return y - x	



###############################


print ("PROBLEMA DE LAS N - REINAS")
print ("#"*26)
print ( "\n")
n = int(input("Introduce el numero de reinas:\n"))
solucion = []
for i in range(n):
	solucion.append(0)
etapa = int(input("Introduce el numero de etapas:\n"))
print (Reinas(solucion, etapa, n))