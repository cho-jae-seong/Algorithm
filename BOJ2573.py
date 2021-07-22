import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs(i,j,visit):
    q=deque()
    q.append([i,j])
    melt_q=deque()
    visit[i][j]=1
    while q:
        i,j=q.popleft()
        melt_cnt=0
        for _ in range(4):
            nx=i+dx[_]
            ny=j+dy[_]
            if 0<=nx<=x-1 and 0<=ny<=y-1 and visit[nx][ny]==0:
                if glacier[nx][ny]!=0:
                    visit[nx][ny]=1
                    q.append([nx,ny])
                else:
                    melt_cnt+=1
        if melt_cnt:
            melt_q.append([i,j,melt_cnt])
    return melt_q

x,y=map(int, sys.stdin.readline().split())
glacier=[list(map(int, sys.stdin.readline().split())) for _ in range(x)]
year=0

while True:
    cnt=0
    visit=[[0 for _ in range(y)] for _ in range(x)]
    for i in range(x-1):
        for j in range(y-1):
            if glacier[i][j]!=0 and visit[i][j]==0:
                cnt+=1
                melt=bfs(i,j,visit)
                while melt:
                    mx,my,m=melt.popleft()
                    glacier[mx][my]=max(glacier[mx][my]-m,0)
    if cnt==0:
        year=0
        break
    if cnt>=2:
        break
    year+=1
print(year)