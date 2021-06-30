import sys
from itertools import combinations

height=[]
for i in range(9):
    a=int(sys.stdin.readline().strip())
    height.append(a)
cb=list(combinations(height,7))
for i in cb:
    if sum(i)==100:
        ans=i
        ans=list(ans)
        ans.sort()
        for j in range(len(ans)):
            print(ans[j])
        break
