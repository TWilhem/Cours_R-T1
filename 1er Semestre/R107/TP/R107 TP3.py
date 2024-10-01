def Exercice1():
    x = "false"
    while x != "Serie" and x != "Parallele":
        x=input("Serie ou Parallele: ")
    R1=float(input("Valeur R1 en ohms: "))
    R2=float(input("Valeur R2 en ohms: "))
    if x == "Serie":
        print(R1+R2)
    if x == "Parallele":
        print((R1*R2) / (R1+R2))
    
    def Parallele(Rep,Rem):
        Re=(Rep*Rem)/(Rep+Rem)
        return(Re)
    
    # Re1=Re2=Re3=Re4=Re5=Re6=Re7=100
    Re1=100
    Re2=200
    Re3=300
    Re4=400
    Re5=500
    Re6=600
    Re7=700
    print(Parallele(Re7,Parallele(Re1,(Re2 + Re3))+Re4+Parallele(Re5,Re6)))


from termcolor import colored
Premier=[]
def NbPremier(Liste):
    for Nb in Liste:
        if Nb != 0:
            Premier.append(Nb)
    print("Les nombres premiers sont :", ', '.join(map(str, Premier)))

def Exercice2():
    MAX = int(input("La liste va de la valeur 0 a : "))
    Liste = [i for i in range(2, MAX+1)]
    print(Liste)
    for x in Liste:
        if x != 0:
            for p in range(x*2, MAX+1, x):
                if p-2 < len(Liste):
                    Liste[p-2] = 0
        
            colored_list = [colored(str(num), 'blue') if num == 0 else str(num) for num in Liste]
            print(' '.join(colored_list))
    NbPremier(Liste)
    print(f"Le nombre de nombre premier: {len(Premier)}")


from collections import Counter

def Divi_Pr(n):
    Divi=[]
    d = 2 
    while n > 1:
        while n % d == 0:
            Divi.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                Divi.append(n)
            break
    return (Divi)


def Pui_Pr(n):
    devid = Divi_Pr(n)
    fact = Counter(devid)
    return [(ime, pow) for ime, pow in fact.items()]


def Exercice3():
    n=int(input("Quel est la valeur que vous souhaitez: "))
    print(f"Les nombres premiers diviseurs sont {Divi_Pr(n)}")
    print(f"Les premieres puissances de chaque diviseurs sont {Pui_Pr(n)}")



print(10*"="+"---"+"Introduction 1"+"---"+10*"=")
# Exercice1()
print(10*"="+"---"+"Crible d'Eratosphène"+"---"+10*"=")
Exercice2()
print(10*"="+"---"+"Décomposition en facteurs premiers"+"---"+10*"=")
# Exercice3()
