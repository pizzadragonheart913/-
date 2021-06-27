n = int(input())

count = 1
a = 0
for i in range(1, 1000000):
    a = i
    if(count > n):
        count -= i
        break
    else:
        count +=i

if(a%2 == 1):
    print((n - count),"/",(a-(n-count)),sep ="")
else:
    print((a-(n-count)),"/",(n - count),sep ="")