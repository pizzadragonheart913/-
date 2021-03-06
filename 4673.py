def notselfnumber(j):
    a = int(j/1000)
    b = int(j/100 - a*10)
    c = int(j/10 - a * 100 - b * 10)
    d = int(j/1 - a * 1000 - b * 100 - c * 10)
    notselfnumber = j + a + b + c + d
    return notselfnumber

lista = []
listb = []
for i in range(1,10000):
    lista.append(i)
for j in range(1,10000):
    a = notselfnumber(j)
    listb.append(a)

newlist = list(sorted(set(lista)-set(listb)))
for i in newlist:
    print(i)