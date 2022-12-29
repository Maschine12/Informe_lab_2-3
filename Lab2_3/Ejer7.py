#7. Un robot puede dar pasos de 1, 2 o 3 metros. Escriba un programa para numerar todas las
#maneras en que el robot camina n metros.
def robot(n):
    if n == 1 or n==2:
        return n
    elif n==3:
        return n+1
    return robot(n-1)+robot(n-2)+robot(n-3)

print(robot(5))