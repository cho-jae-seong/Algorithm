import sys
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    move_q=deque()
    q.append([x,y])
    check[x][y]=1
    total=0
    cnt=0
    while q:
        x,y=q.popleft()
        move_q.append([x,y])
        total+=people[x][y]
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not check[nx][ny]:
                if l<=abs(people[x][y]-people[nx][ny])<=r:
                    q.append([nx,ny])
                    check[nx][ny]=cnt
    while move_q:
        x,y=move_q.popleft()
        people[x][y]=total//cnt
    if cnt==1:
        return 0
    return 1


n,l,r=map(int, sys.stdin.readline().split())
people=[list(map(int, sys.stdin.readline().split()))for i in range(n)]
ans=0
while True:
    q=deque()
    cnt=0
    check=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                cnt+=bfs(i,j)
    if not cnt:
        break
    ans+=1
print(ans)