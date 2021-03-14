a = str(input())

for i in range(97, 123):
    k = a.find(chr(i))
    if(k!= -1):
        print(a.index(chr(i)), end = ' ')
    else:
        print(-1, end = ' ')