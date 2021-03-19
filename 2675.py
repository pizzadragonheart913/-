a = int(input())
for i in range(a):
    R, S = input().split()
    R = int(R)
    S = list(S)
    for j in range(len(S)):
        print(S[j]*R, end ="")
    print()