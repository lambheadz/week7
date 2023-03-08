'''
s = input()
d = s[::-1]
if s == d:
    print('yes')
else:
    print('no')
'''

s = input()
d = ''.join(reversed(s))
if s == d:
    print('yes')
else:
    print('no')