import sys
from collections import deque

def bfs(start):
    cnt=0
    queue=deque()
    queue.append(start)
    visited=[0]*(n+1)
    visited[start]=1
    while queue:
        now=queue.popleft()
        cnt+=1
        for g in graph[now]:
            if not visited[g]:
                visited[g]=1
                queue.append(g)
    return cnt

n,m=map(int, sys.stdin.readline().split())
graph=[[]for _ in range(n+1)]
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[b].append(a)
maximum=0
result=[]
for i in range(1,n+1):
    if graph[i]:
        tmp=bfs(i)
        if maximum<=tmp:
            if maximum<tmp:
                result=[]
            maximum=tmp
            result.append(i)
print(*result)