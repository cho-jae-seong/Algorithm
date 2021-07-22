import sys
from collections import deque

n,m,k,x=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
answer=[]
queue=deque()
queue.append((x,0))
visited[x]=True
while queue:
    cur,cnt=queue.popleft()
    if cnt==k:
        answer.append(cur)
    elif cnt<k:
        for g in graph[cur]:
            if not visited[g]:
                visited[g]=True
                queue.append((g,cnt+1))
if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for ans in answer:
        print(ans)