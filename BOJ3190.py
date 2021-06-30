import sys
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def change(d,c):
    if c=="L":
        d=(d+3)%4
    else:
        d=(d+1)%4
    return d



def snake():
    x,y=0,0
    direction=1
    visited=deque()
    visited.append([x,y])
    apple[x][y]=2
    time=1
    while True:
        x,y=x+dx[direction],y+dy[direction]
        if 0<=x<n and 0<=y<n and apple[x][y]!=2:
            if not apple[x][y]==1:
                temp_x,temp_y=visited.popleft()
                apple[temp_x][temp_y]=0
            apple[x][y]=2
            visited.append([x,y])
            if time in dir_change.keys():
                direction=change(direction,dir_change[time])
            time+=1
        else:
            return time


n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
apple=[[0]*n for i in range(n)]
for i in range(k):
    a,b=map(int, sys.stdin.readline().split())
    apple[a-1][b-1]=1
l=int(sys.stdin.readline())
dir_change={}
for i in range(l):
    x,c=map(str, sys.stdin.readline().split())
    dir_change[int(x)]=c
print(snake())