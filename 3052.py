array = []
newarray = []
for i in range(10):
    array.append(int(input())) #입력받은 배열

for j in range(0,10,1):
    newarray.append(array[j] % 42) # 42로 나눠서 새 배열을 만듦

newset = set(newarray)

print(len(newset))