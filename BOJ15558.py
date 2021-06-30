import sys
from collections import deque

def bfs(start):
    q=deque([start])
    cur_idx=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for next_x,next_y in ((x,y+1),(x,y-1),(~x,y+k)):
                if next_y>=n:
                    return 1
                if cur_idx<next_y<n and board[next_x][next_y] and not visited[next_x][next_y]:
                    q.append((next_x,next_y))
                    visited[next_x][next_y]=True
        cur_idx+=1
    return 0

n,k=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().strip())) for _ in range(2)]
visited=[[False]*n for _ in range(2)]
print(bfs([0,0]))
