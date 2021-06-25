n = int(input())

level = 1
if(n == 1):
    print(1)
else:
    n -= 1
    while(1):
        if (n - 6 * level <=0):
            print(level +1)
            break
        else:
            n -= 6* level
            level += 1