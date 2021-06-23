n = int(input())
inputword = []
i=0
while (i < n):
    inputword.append(str(input()))
    i+=1

index =0
count=0
word=[]
for i in inputword:# 단어수만큼 반복
    setalphabet = []
    word = inputword[index]
    if(len(word) ==1):
        count +=1
    else:
        setalphabet.append(word[0])
        count +=1
        for j in range(0,len(word)-1): #한 단어를 처음부터 마지막까지
            if(word[j] != word[j+1]): # j번째와 j+1번째 단어를 비교해서 다르면?
                if(setalphabet.count(word[j+1]) == 0): # j와 j+1이 다르고 이미 나온적 있는지 체크하는데 없을경우
                    setalphabet.append(word[j+1])# 없었으니깐 삽입 한다.
                    continue
                else:
                    count -= 1
                    break
            else:
                continue             
    index +=1
print(count)