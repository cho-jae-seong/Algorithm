import sys
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny]=2

m,n=map(int, sys.stdin.readline().split())
graph = [list(map(int, list(input()))) for _ in range(m)]
for j in range(n):
    if graph[0][j]==0:
        bfs(0,j)
print('YES' if 2 in graph[-1] else 'NO')
