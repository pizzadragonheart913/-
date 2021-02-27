A = int(input())
B = int(input())
C = int(input())
intanswer = A*B*C
answer = str(intanswer)

for i in range(10):
    result = 0
    for j in range(len(answer)):
        if(i==int(answer[j])):
            result = result + 1
    print(result)
    