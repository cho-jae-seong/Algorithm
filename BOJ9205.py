import sys
from collections import deque

def bfs(x,y):
    q=deque()
    check=[]
    q.append([x,y,20])
    check.append([x,y,20])
    while q:
        x,y,beer=q.popleft()
        if x==dx and y==dy:
            print("happy")
            return
        for nx,ny in d:
            if [nx,ny,20] not in check:
                l1=abs(nx-x)+abs(ny-y)
                if beer*50>=l1:
                    q.append([nx,ny,20])
                    check.append([nx,ny,20])
    print("sad")
    return

t=int(sys.stdin.readline().strip())
for i in range(t):
    n=int(sys.stdin.readline().strip())
    sx,sy=map(int, sys.stdin.readline().split())
    d=[]
    for _ in range(n):
        x,y=map(int, sys.stdin.readline().split())
        d.append([x,y])
    dx,dy=map(int, sys.stdin.readline().split())
    d.append([dx,dy])
    bfs(sx,sy)