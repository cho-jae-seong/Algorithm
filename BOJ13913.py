import sys
from collections import deque

def bfs(start,target):
    q=deque()
    q.append((n,0))
    visit[start]=start
    while q:
        cur,time=q.popleft()
        if cur==target:
            idx=cur
            while idx!=start:
                path.append(idx)
                idx=visit[idx]
            path.append(start)
            return time
        if cur+1<100001 and visit[cur+1]==-1:
            q.append((cur+1,time+1))
            visit[cur+1]=cur
        if cur-1>=0 and visit[cur-1]==-1:
            q.append((cur-1,time+1))
            visit[cur-1]=cur
        if cur*2<100001 and visit[cur*2]==-1:
            q.append((cur*2,time+1))
            visit[cur*2]=cur

n,k=map(int, sys.stdin.readline().split())
visit=[-1 for i in range(100001)]
path=[]
print(bfs(n,k))
print(*path[::-1])