import sys
import copy
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=0

def bfs():
    global ans
    w=copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if w[i][j]==2:
                q.append([i,j])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if w[nx][ny]==0:
                    w[nx][ny]=2
                    q.append([nx,ny])
    cnt=0
    for i in w:
        cnt+=i.count(0)
    ans=max(ans,cnt)

def combination(x):
    if x==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                combination(x+1)
                board[i][j]=0

n,m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for i in range(n)]
q=deque()
combination(0)
print(ans)