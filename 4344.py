import sys

c = int(input())
score = []

for i in range(c):
    score = list(map(int, sys.stdin.readline().strip().split()))
    avg = (sum(score) - score[0])/score[0]
    cnt = 0
    for j in range(1,len(score)):
        if(score[j]>avg):
            cnt += 1
    answer = (cnt / score[0])*100
    print('%.3f'% answer,end="")
    print("%")