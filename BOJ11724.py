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

n,m=map(int, sys.stdin.readline().split())
#arr=[list(map(int, input().split())) for _ in range(m)]
unf=dict()
for i in range(1,n+1):
    unf[i]=i
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    union(a,b)
answer=0
for i in range(1,n+1):
    if i==unf[i]:
        answer+=1
print(answer)


