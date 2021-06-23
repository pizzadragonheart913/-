n = int(input())
scorelist = map(int,input().split())
score= list(scorelist)
m = max(score)
sum =0
for i in range(n):
    new = score[i]/m
    new *= 100
    sum += new

print(sum / n)