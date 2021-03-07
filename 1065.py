n = int(input())
cnt = 0

def hannumber(j):
    global cnt
    a = int(j/100 )
    b = int(j/10 - a * 10)
    c = int(j/1 - a * 100 - b * 10)
    if(a == 0):
        cnt += 1
    else:
        if(float((a+c)/2) == b):
            cnt += 1
    return cnt

for i in range(1,n+1):
    hannumber(i)
print(cnt)