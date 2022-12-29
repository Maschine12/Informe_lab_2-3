#Implemente la selección por orden como un programa: El algoritmo de selección por
#orden acomoda la sucesión s1, . . . , sn en orden no decreciente, para ello encuentra primero
#el elemento más pequeño, por ejemplo si, y lo coloca en el primer lugar intercambiando
#s1 y si. después encuentra el algoritmo más pequeño en s2, . . . , sn, de nuevo digamos si, y
#lo coloca en el segundo lugar intercambiando s2 y si. Continua hasta que la sucesión esté
#ordenada.
import random
l=[]
for i in range(20): 
    ran= random.randrange(50)
    l.append(ran)

def selectionSort(L):
    for i in range(len(L)):
        lis = i
        for j in range(i+1, len(L)):
            if L[j] < L[lis]:
                lis = j
        print(l)    
        
selectionSort(l)

