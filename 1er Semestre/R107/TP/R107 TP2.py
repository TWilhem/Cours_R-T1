def Exercice1():
    Somm=0
    PairG=0
    Auto="Yes"
    SoPaire=0
    NbReel=int(input("Combien de Nombre réel souhaitez vous fournir: "))
    fournit=input("Quel est la liste de nombre a rentrer (a rentrer les un après les autres espacé d'un espace sur la même ligne): ")
    FList=fournit.split(" ")
    for i in range(len(FList)):
        Somm+=float(FList[i])
        while float(FList[i])%1 == 0 and float(FList[i]) > 0:
            if int(FList[i])%2 == 0:
                print(f"{FList[i]} est un nombre pair")
                SoPaire+=1
                if PairG < int(FList[i]) and Auto == "Yes":
                    PairG = int(FList[i])
            break
        if float(FList[i])%1 != 0 or float(FList[i]) < 0:
            print(f"{FList[i]} n'est pas un entier naturel")
            Auto = "NO"

    print(f"La Somme des nombres de la liste est de {Somm}")
    print(f"La Moyenne des nombres de la liste est de {Somm/(len(FList))}")
    print(f"Il y a {SoPaire} nombre paire")
    if PairG != 0 and Auto == "Yes":
        print(f"Le chiffre pair le plus grand est le {PairG}")
    if PairG == 0 and Auto == "Yes":
        print(f"il n'y a pas de chiffre entier pair")
    if Auto == "NO":
        print("il y a un nombre non entier naturel")


def Exercice2():
    NbWorld=1
    Phrase=input("Donnez moi une phrase: ")
    for i in reversed(Phrase):
        if " " in i:
            NbWorld+=1
        print(i, end='')
    print()
    print(f"il y a {NbWorld} mots dans cette phrase")

    for Letter in range(ord('a'), ord('z')+1):
        print(f"{Letter} : {chr(Letter)}, {Letter-32} : {chr(Letter-32)} ")

    for i in Phrase:
        ChAsc = ord(i)
        if ChAsc >= 97 and ChAsc <= 122:
            print(chr(ChAsc-32), end='')
        if ChAsc >= 65 and ChAsc <= 90:
            print(chr(ChAsc+32), end='')
        if ChAsc == 32:
            print(chr(ChAsc), end='')
    print()

    
    count = sum(1 for mot in Phrase if mot[0].isupper())
    print(f"il y a {count} mot avec une majuscule")


def Exercice3():
    Som=0
    SommNomb=0
    TotaSom=0
    TotaSom2=0
    TotaSom3=0
    NombreS=input("Donnez moi un nombre: ")
    for i in NombreS:
        Som+=int(i)
    print(f"Voici la somme des chiffres du nombres: {Som}")

    for i in range(0, 1000):
        for Numb in str(i):
            SommNomb+=int(Numb)
        if SommNomb < 11 or SommNomb > 11:
            SommNomb = 0
        if SommNomb == 11:
            TotaSom+=1
    print(f"Nombre de Somme: {TotaSom}")

    for i in range(0, 1000):
        if ("6" in str(i) and "1" not in str(i)) or ("1" in str(i) and "6" not in str(i)):
            TotaSom2+=1
    print(f"Nombre de nombre contenant soit 6 soit 1: {TotaSom2}")

    for i in range(0, 1000):
        if str(i) == str(i)[::-1]:
            TotaSom3+=1
    print(f"Nombre de nombre miroir: {TotaSom3}")


print(10*"="+"---"+"Exercice 1"+"---"+10*"=")
Exercice1()
print(10*"="+"---"+"Exercice 2"+"---"+10*"=")
# Exercice2()
print(10*"="+"---"+"Exercice 3"+"---"+10*"=")
# Exercice3()