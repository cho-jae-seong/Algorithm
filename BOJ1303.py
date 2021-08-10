import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,char):
    q=deque()
    q.append((x,y))
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and visit[nx][ny]==0 and war[nx][ny]==char:
                q.append((nx,ny))
                visit[nx][ny]=1
                cnt+=1
    return cnt

n,m=map(int, sys.stdin.readline().split())
war=[list(sys.stdin.readline().strip()) for _ in range(m)]
visit=[[0]*n for _ in range(m)]
white=0
blue=0
for i in range(m):
    for j in range(n):
        if visit[i][j]==0:
            visit[i][j]=1
            temp=bfs(i,j,war[i][j])
            if war[i][j]=='W':
                white+=(temp*temp)
            else:
                blue+=(temp*temp)
print(white,blue)