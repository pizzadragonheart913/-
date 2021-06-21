import sys

string = sys.stdin.readline()
string = string.upper()

cnt =[]
i = 65
while (i < 91):
    c = string.count(chr(i))
    cnt.append(c)
    i+=1

big = chr(cnt.index(max(cnt))+65)

cnt.sort(reverse = True)

if(cnt[0] == cnt[1]):
    print("?")

else:
    print(big)