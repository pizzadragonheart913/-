import sys

string = sys.stdin.readline()
a = string.count("c=")
b = string.count("lj")
c = string.count("z=")
d = string.count("dz=")
e = string.count("c-")
f = string.count("d-")
g = string.count("nj")
h = string.count("s=")
print(len(string)-a-b-c-d-e-f-g-h-1)