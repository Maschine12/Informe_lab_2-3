#Implemente un programa recursivo que sume dos números a + b. Considera que la suma
#a+b = a + 1 + 1 + ...+ 1 (b veces)

def suma(a,b):
    if b == 0:
        return a
    return suma(a,b-1) +1
print(suma(4,3))