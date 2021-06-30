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
        unf[b]=a

def check(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return 1
    else:
        return 0

v,e=map(int, sys.stdin.readline().split())
g=[]
answer=0
unf=[i for i in range(v+1)]
for i in range(e):
    a,b,c=map(int, sys.stdin.readline().split())
    g.append([a,b,c])
g.sort(key=lambda x:x[2])
for i in range(e):
    if check(g[i][0],g[i][1])==0:
        answer+=g[i][2]
        union(g[i][0],g[i][1])
print(answer)