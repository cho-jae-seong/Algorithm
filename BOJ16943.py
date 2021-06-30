from itertools import permutations
import sys

a,b = sys.stdin.readline().split()
b = int(b)
lst = list(map(''.join, list(permutations(a))))
c = -1
for num in lst:
    first = num[0]
    num = int(num)
    if b>= num and first != '0':
        c = max(c, num)
print(c)


