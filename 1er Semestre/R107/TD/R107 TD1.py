def IMC():
    taille=float(input("Ta taille en mètres: "))
    masse=float(input("Ta masse en Kg: "))

    IMC = masse/(taille**2)

    print(IMC)

    if IMC > 25:
        print("you are fatt")
    else:
        print("tranquille")

# IMC()

from math import sqrt

print("aX²+bX+c")
a=float(input("A= "))
b=float(input("B= "))
c=float(input("C= "))

delta = (b**2)-4*a*c

if delta < 0:
    print("pas de racine")
if delta > 0:
    resu1=(-b-sqrt(delta)/2*a)
    resu2=(-b+sqrt(delta)/2*a)
    print(f'les racines sont égales a {resu1} et {resu2}')
if delta == 0:
    result=(-b/2*a)
    print(f'la seul racine est égale a: {result}')
