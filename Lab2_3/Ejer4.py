#Escriba un programa recursivo y otro no recursivo para calcular n!. Compare los tiempos
#requeridos por los programas.
#factorial
import time
def factorial(n):
    r = 1
    i = 2
    while i<=n:
        r*=i
        i +=1
    return r
def factorial_recursivo(n):
    #cuando n =0
    if n ==0:
        return 1
    return n*factorial_recursivo(n-1)

inicio = time.time()
time.sleep(1)
factorial(200)
fin = time.time()
print("Tiempo de ejecucion del factorial no recursivo")
print((fin-inicio))


inicio1=time.time()
time.sleep(1) #nos ayudara a ver de manera mas precisa cual es mas rapido
factorial_recursivo(200)
fin2=time.time()
print("Tiempo de ejecucion de factorial recursivo")
print((fin2-inicio1))
