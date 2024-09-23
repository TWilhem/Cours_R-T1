# x=0
# while x<21:
#     print(x)
#     x+=2

# for x in range(30,12,-3):
#     print(x)

# for x in range(0,3):
#     for y in range(0,2):
#         print(x, y)

# y=[]
# for x in range(0,5):
#     y.append(x)
#     print(y)

##################-----2-----#####################
r=[5,9,7,3,15,8]
# l=0
# for y in r:
#     # print(y)
#     v=int(y)
#     l+=v
# print(l)

# r.append(4)
# print(r)

# print(len(r))

# for y in range(0,len(r)):
#     if r[y]%3 == 0:
#         print(y)
#         r[y]=0
# print(r)

##################-----3-----#####################

# mot=str('message secret')
# for i in range(len(mot)):
#     if i%2 != 0:
#         print(mot[i])

# mot=str('Sesame ouvre-toi')
# for i in range(len(mot)):
#     print(mot[len(mot)-i-1])

# mot=str('message secret')
# for i in range (len(mot)):
#     print(ord(mot[i]))
list1=[]
mot=str('LNLRNBCDWVNBBJPNLQROOAN')
for i in range (len(mot)):
    num = (ord(mot[i]) - 9)
    if num < 65:
        print('lol')
        num+=26
    list1.append(chr(num))
print(list1)