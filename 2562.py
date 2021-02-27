emptylist = []

for i in range(0,9,1):
    emptylist.append(int(input()))

print(max(emptylist))
print(emptylist.index(max(emptylist))+1)