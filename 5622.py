import sys

string = sys.stdin.readline()
callnum = []
for i in string:
    if (i=='A'or i=='B'or i=='C'):
        callnum.append(2)
    elif (i=='D'or i=='E'or i=='F'):
        callnum.append(3)
    elif (i=='G'or i=='H'or i=='I'):
        callnum.append(4)
    elif (i=='J'or i=='K'or i=='L'):
        callnum.append(5)
    elif (i=='M'or i=='N'or i=='O'):
        callnum.append(6)
    elif (i=='P'or i=='Q'or i=='R' or i=='S'):
        callnum.append(7)
    elif (i=='T'or i=='U'or i=='V'):
        callnum.append(8)
    elif (i=='W'or i=='X'or i=='Y' or i=='Z'):
        callnum.append(9)

allsum = sum(callnum)+len(callnum)
print(allsum)