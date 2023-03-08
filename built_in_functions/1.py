import math
s = int(input())
p = 1
l = []
for i in range(s):
    e = input()
    l.append(int(e))
res = math.prod(l)
print(res)
'''for x in l:
    p *= int(x)
print(p)'''