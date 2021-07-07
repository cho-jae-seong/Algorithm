import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    cnt=1
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==1 and not visited[nx][ny]:
                    cnt+=1
                    visited[nx][ny]=1
                    queue.append((nx,ny))
    return cnt

n,m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split()))for _ in range(n)]
visited=[[0]*m for _ in range(n)]
count=0
wide=0
for i in range(n):
    for j in range(m):
        if board[i][j]==1 and not visited[i][j]:
            count+=1
            wide=max(wide,bfs(i,j))
print(count)
print(wide)
