#Escriba un programa recursivo y otro no recursivo para calcular la sucesión deFibonacci.
#Compare los tiempos requeridos por los programas
import time
def fibonacci_normal(n):
    a=0
    b=1
    #cambi haciendo uso de un 3er elemento
    for i in range(n):
        c=a+b
        a=b
        b=c
    return a    
def fibonacci_recursivo(n):
    if n<2:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

#tiempo de ejecucion
ini = time.time()
time.sleep(1)
fibonacci_normal(20)
fin=time.time()
print(fin-ini)
#tiempo de ejecucion del recursivo
inic = time.time()
time.sleep(1)
fibonacci_recursivo(20)
fi=time.time()
print(fi-inic)