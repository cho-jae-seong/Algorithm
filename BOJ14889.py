import sys
from itertools import combinations

n=int(sys.stdin.readline())
sl=[list(map(int, sys.stdin.readline().split())) for i in range(n)]
cb=combinations(range(n),n//2)
ans=sys.maxsize

for c in cb:
    a=set(c)
    b=list(set(range(n))-a)
    a=list(a)
    start,link=0,0
    for i in range(n//2-1):
        for j in range(i+1,n//2):
            start+=sl[a[i]][a[j]]+sl[a[j]][a[i]]
            link+=sl[b[i]][b[j]]+sl[b[j]][b[i]]
    ans=min(ans,abs(start-link))
print(ans)