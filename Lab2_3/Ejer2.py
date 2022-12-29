#Corra el algoritmo anterior “desordena” (del ejercicio 1) muchas veces para la misma
#sucesión de entrada. ¿Como puede analizarse la salida para determinar si es
#verdaderamente “aleatorio”?
import random
def desordenada(n):
    lis=[i for i in range(n)]
    na = random.randrange(n)
    #intercambio
    for j in lis:
        j=j+1
        if j <n:
            c = lis[j]
            lis[j] = lis[na]
            lis[na]=c
            j=j+2
        else:
            j=0
    print(lis[1:n])
for i in range(20):
    desordenada(50)
"""
Al observar dicho algoritmo del ejercicio 1, podemos decir que el resultado del cambio de
numeros alrededor de una lista es completamente aleatoria, ya que los datos mostrados no llevan 
alguna similitud con los siguientes
no existe patron visible que nos diga que dicho patron sea una lista no "aleatoria" 
"""