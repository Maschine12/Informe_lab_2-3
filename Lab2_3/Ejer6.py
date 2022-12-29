def robot(n):
    if n==1 or n==2: #caso base en el cual el camino minimo que puedes 
        #recorrer con estas reglas es un de 2 
        return n # se retornara el caso base
    return robot(n-1) + robot(n-2)

print(robot(5))