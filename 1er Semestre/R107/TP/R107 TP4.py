def Exercice1():
    # a=123 nombre
    # a='123' Chaine de caractere

    # non car les variables a et b ne sont pas defini

    L=[1,2,3,4,5,6,7,8,9,10]
    print(L[5])

    liste = ""
    for val in L:
        liste += f'{val},'
    print(liste)

    liste2 = ""
    for val2 in L[5:]:
        liste2 += f'{val2},'
    print(liste2)

    up = 0
    liste3 = ""
    val3 = 0
    while val3 != 7:
        val3 = L[up]
        liste3 += f'{val3},'
        if up < len(L)-1:
            up += 1
        else:
            print('fin de liste')
            break
    print(liste3)

    for chiffre in L:
        if chiffre % 2 != 0:
            print(f'{chiffre} est impaire')
        elif (chiffre % 2) == 0:
            print(f'{chiffre} est paire')

def Exercice2():
    f1=open("./1er Semestre/R107/TP/source.txt","w", encoding='utf8')
    f1.write('SUPER ! Je viens de créer mon premier fichier !\n')
    f1.write("ma deuxieme ligne")
    f1.close()

    f2=open("./1er Semestre/R107/TP/source.txt","r", encoding='utf8')
    s=f2.readlines()
    f2.close()
    f3=open("./1er Semestre/R107/TP/destination.txt","w",encoding='utf8')
    f3.writelines(s)
    f3.close()

def Exercice3(): 
    for i in range(33, 256):
        if i <= 126 or i >= 161:
            print(f"{i} : {chr(i)}")

def Exercice4():
    f4=open("./1er Semestre/R107/TP/source.txt","r", encoding='utf8')
    k=f4.readlines()
    f4.close()
    f5=open("./1er Semestre/R107/TP/message_code.txt","w", encoding='utf8')
    for line in k:
        for lettre in line:
            code = ord(lettre)
            code+=1
            letCode = chr(code)
            k=f5.writelines(letCode)
    f5.close()

    
    f6=open("./1er Semestre/R107/TP/message_secret.txt","r", encoding='utf8')
    b=f6.readlines()
    f6.close()
    for NbCode in range(-4,5,1):
        Pdecode = ""
        if NbCode != -1:
            for line in b:
                for lettre in line:
                    decode = ord(lettre)
                    if decode <= 126 or decode >= 161 or decode >= 33:
                        Pdecode += chr(decode + NbCode)
            print(f"Solution a {NbCode} {Pdecode}")
        if "BRAVO" in Pdecode: 
            f7=open("./1er Semestre/R107/TP/message_decode.txt","w", encoding='utf8')
            f7.writelines(Pdecode)
            f7.close



print(10*"="+"---"+"révision flash"+"---"+10*"=")
# Exercice1()
print(10*"="+"---"+"Les fichiers"+"---"+10*"=")
# Exercice2()
print(10*"="+"---"+"le code ASCII"+"---"+10*"=")
# Exercice3()
print(10*"="+"---"+"Cryptons, cryptons !"+"---"+10*"=")
Exercice4()