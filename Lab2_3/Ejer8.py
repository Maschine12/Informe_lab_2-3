#8. Implemente un programa recursivo que calcule la potencia de un nu mero elevado a otro.
#Sabemos que 2n = 2n/2. 2n/2 donde n es un nro par; y 2n = 2(n-1)/2. 2(n-1)/2.2 si n es
#impar

# n base
# m exponente

def potencia(n,m):
    if m==0:
        return 1
    elif n==0:
        return 0
    elif m ==1:
        return n
    else:
        return n * potencia(n,(m-1))
print(potencia(2,5))