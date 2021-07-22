import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global answer
    temp=0
    q=deque()
    q.append((x,y))
    temp+=1
    board[x][y]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
                temp+=1
                q.append((nx,ny))
                board[nx][ny]=2
    if answer<temp:
        answer=temp

n,m,k=map(int, sys.stdin.readline().split())
board=[[0]*m for _ in range(n)]
answer=0
for i in range(k):
    r,c=map(int, sys.stdin.readline().split())
    board[r-1][c-1]=1
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            bfs(i,j)
print(answer)