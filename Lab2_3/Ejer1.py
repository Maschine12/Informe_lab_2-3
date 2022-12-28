#1. Implemente el siguiente algoritmo como un programa para desordenar.
import random
def desordenada(n):
    lis=[i for i in range(n)]
    na = random.randrange(n)
    #intercambio
    for j in lis:
        if j <n:
            c = lis[j]
            lis[j] = lis[na]
            lis[na]=c
        else:
            j=-1
        
    print(lis)

desordenada(35)