def Exercice1():
    Somm=0
    NbReel=int(input("Combien de Nombre réel souhaitez vous fournir: "))
    fournit=input("Quel est la liste de nombre a rentrée: ")
    FList=fournit.split(" ")
    print(FList)
    print(len(FList))
    for i in range(len(FList)):
        Somm+=int(FList[i])
    print(f"La Somme des nombres de la liste est de {Somm}")
    print(f"La Moyenne des nombres de la liste est de {Somm/(len(FList))}")


print(10*"="+"---"+"Exercice 1"+"---"+10*"=")
Exercice1()