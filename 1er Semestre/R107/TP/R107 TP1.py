def Structures1():
    defini=input("jour ou seconde: ")
    if defini == "jour":
        secondeT=int(input("nombre de seconde: "))
        MinuteT = secondeT/60
        secondeT = secondeT%60
        HeureT = MinuteT/60
        MinuteT = MinuteT%60
        JourT = HeureT/24
        HeureT = HeureT%24
        print(f"{int(JourT)} Jour {int(HeureT)} Heure {int(MinuteT)} Minute {int(secondeT)} Seconde")

    elif defini == "seconde":
        Jour=int(input("nombre de jour: "))
        heure=int(input("nombre de heure: "))
        minute=int(input("nombre de minute: "))
        seconde=int(input("nombre de seconde: "))
        SecondeF = (Jour*24*3600) + (heure*3600) + (minute*60) + (seconde)
        print(f"Cela fait {SecondeF} secondes")

def Structures2():
    taille=float(input("Ta taille en mètres: "))
    masse=float(input("Ta masse en Kg: "))
    IMC = masse/(taille**2)
    print(f"Ton IMC est de {int(IMC)}")
    if IMC > 25:
        print("Trop Gros")
    else:
        print("Normal")

from math import sqrt
def Structures3():
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

def Structures4():
    Tfahrenheit = int(input("quel est la valeur en fahrenheit: "))
    Tdegres = (Tfahrenheit - 32)*5/9
    print(f"La temperature {Tfahrenheit} fahrenheit en degrés celcuis fait: {Tdegres}°C")


liste=[5,8,3,7,11,2]
def boucles1():
    for i in liste:
        print("*"*i)


def boucles2():
    max_valeur = max(liste)
    for ligne in range(max_valeur, 0, -1):
        for nombre in liste:
            if nombre >= ligne:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

import math
def Hydre():
    coup = 1
    NbTête=int(input("Nombre de tête de L'hydre: "))
    while NbTête > 0:
        if NbTête <= 0:
            print("Hydre déjà mort")
            break
        NbTêteR = math.ceil(NbTête/2)
        if coup == 1:
            print(f"Si l'Hydre a {NbTête} têtes, Hercule en coupe la moitié au premier coup d'épée. Il en reste {NbTêteR}")
        elif coup == 2:
            print(f"Au second coup d'épée, Hercule en coupe {NbTêteR}. Il en reste {NbTêteR}")
        else:  
            print(f"Au {coup}e coup d'épée, Hercule coupe {NbTêteR} têtes. Il en reste {NbTêteR}. Rien ne repousse.")
        coup += 1

        if NbTêteR == 1:
            print(f"L'Hydre a été achevé, il a été tué en {coup} coups")
            break

        if NbTêteR%2 != 0:
            NbTête = NbTêteR*3+1
            print(f"Instantanément, le nombre de têtes triple et il en pousse une autre. Il y a maintenant {NbTête} têtes.")
        else:
            NbTête = NbTêteR
            print("rien ne repousse")



def Explosif():
    NbExplosif=int(input("Donner un nombre a 6 chiffre: "))
    if NbExplosif > 999999 or NbExplosif < 100000:
        print("erreur")
    U= int(str(NbExplosif)[:3])
    N = int(str(NbExplosif)[3:])

    for _ in range(N):
        print(f"{U} --> {U*13} --> {str(U*13)[-3:]}")
        U = int(str(U*13)[-3:])

print(10*"="+"---"+"Structures 1"+"---"+10*"=")
# Structures1()
print(10*"="+"---"+"Structures 2"+"---"+10*"=")
# Structures2()
print(10*"="+"---"+"Structures 3"+"---"+10*"=")
# Structures3()
print(10*"="+"---"+"Structures 4"+"---"+10*"=")
# Structures4()
print(10*"="+"---"+"Boucle 1"+"---"+10*"=")
# boucles1()
print(10*"="+"---"+"Boucle 2"+"---"+10*"=")
boucles2()
print(10*"="+"---"+"L'Hydre"+"---"+10*"=")
# Hydre()
print(10*"="+"---"+"Explosif"+"---"+10*"=")
# Explosif()