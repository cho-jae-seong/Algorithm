import sys

def find(v):
    if unf[v]==v:
        return v
    else:
        unf[v]=find(unf[v])
        return unf[v]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        unf[a]=b
    return

def check(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return 1
    else:
        return 0

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
graph=[]
unf=[i for i in range(n+1)]
answer=0
for i in range(m):
    a,b,c=map(int, sys.stdin.readline().split())
    graph.append([a,b,c])
graph.sort(key=lambda x:x[2])
for i in range(len(graph)):
    if check(graph[i][0],graph[i][1])==0:
        answer+=graph[i][2]
        union(graph[i][0],graph[i][1])
print(answer)