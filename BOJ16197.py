import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x1,y1,x2,y2,cnt):
    q=deque()
    q.append((x1,y1,x2,y2,cnt))
    while q:
        x1,y1,x2,y2,cnt=q.popleft()
        if cnt>=10:
            return -1
        for i in range(4):
            nx1=x1+dx[i]
            ny1=y1+dy[i]
            nx2=x2+dx[i]
            ny2=y2+dy[i]
            if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:
                if board[nx1][ny1]=='#':
                    nx1,ny1=x1,y1
                if board[nx2][ny2]=='#':
                    nx2,ny2=x2,y2
                q.append((nx1,ny1,nx2,ny2,cnt+1))
            elif 0<=nx1<n and 0<=ny1<m:
                return cnt+1
            elif 0<=nx2<n and 0<=ny2<m:
                return cnt+1
            else:
                continue
    return -1

n,m=map(int, sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
temp=[]
for i in range(n):
    for j in range(m):
        if board[i][j]=='o':
            temp.append((i,j))
print(bfs(temp[0][0],temp[0][1],temp[1][0],temp[1][1],0))

