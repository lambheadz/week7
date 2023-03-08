s = input()
u_cnt = 0
l_cnt = 0
for x in s:
    if x.islower():
        l_cnt += 1
    elif x.isupper():
        u_cnt += 1
print(l_cnt)
print(u_cnt)