import sys

string = sys.stdin.readline()
string = reversed(string)
listedstring = list(string)
tokenstring = "".join(listedstring)
a = tokenstring[1:4:1]
b = tokenstring[5:8:1]
if (a>b):
    print(a)
else:
    print(b)