import sys

def find(v):
    if v==unf[v]:
        return v
    else:
        unf[v]=find(unf[v])
        return unf[v]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        unf[a]=b

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())

unf=dict()
for i in range(1,n+1):
    unf[i]=i

for x in range(1,n+1):
    maps=list(map(int, sys.stdin.readline().split()))
    for y in range(1,len(maps)+1):
        if maps[y-1]==1:
            union(x,y)
tour=list(map(int, sys.stdin.readline().split()))
result=set([find(i) for i in tour])
if len(result)!=1:
    print("NO")
else:
    print("YES")
