import sys
from collections import deque

f,s,g,u,d=map(int, sys.stdin.readline().split())
visit=[0]*(f+1)
q=deque()
q.append((s,0))
visit[s]=1
while q:
    idx,cnt=q.popleft()
    if idx==g:
        print(cnt)
        exit(0)
    else:
        if idx+u<=f and visit[idx+u]==0:
            q.append((idx+u,cnt+1))
            visit[idx+u]=1
        if idx-d>=1 and visit[idx-d]==0:
            q.append((idx-d,cnt+1))
            visit[idx-d]=1
print("use the stairs")
