t = int(input())#횟수
x = []

for i in range(0,t): #횟수만큼 반복
    h, w, n = map(int,input().split()) # 3개 입력받기
    if(n%h==0):
            floor = str(int(h))
            ho = str(int(n/h))
    elif(h*w == n):
        floor = str(int(h))
        ho = str(int(w))
    else:
        floor = str(int(n%h))
        ho = str(int(n/h + 1))

    if(len(ho)==1):
        ho = "0" + ho
        x.append(floor + ho)
    else:
        x.append(floor + ho)

for i in x:
    print(i)