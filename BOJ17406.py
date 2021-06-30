import sys
from itertools import permutations
from collections import deque
from copy import deepcopy
import math

y,x,n=map(int, sys.stdin.readline().split())
original_maps=[list(map(int, sys.stdin.readline().split()))for _ in range(y)]
arrs=[list(map(int, sys.stdin.readline().split()))for _ in range(n)]

candidates=permutations(arrs, len(arrs))

def get_A(maps):
    return min([sum(maps[y]) for y in range(len(maps))])

def get_square(maps,r,c,s):
    dirs=[(0,1), (1,0), (0,-1), (-1,0)]
    queue=deque()
    length=s*2+1
    start=(r-s,c-s)
    count=1
    idx=0
    dy,dx=dirs[idx]
    while True:
        y,x=start
        queue.append(start)
        ny,nx=y+dy,x+dx
        count+=1
        start=ny,nx
        if count==length:
            count=1
            idx+=1
            if idx==len(dirs):
                break
            dy,dx=dirs[idx]
    return queue

maps=deepcopy(original_maps)
mins=math.inf
for each_case in candidates:
    maps=deepcopy(original_maps)
    for order in each_case:
        r,c,s=order
        r-=1
        c-=1
        for i in range(1,s+1):
            coords=get_square(maps,r,c,i)
            values=deque([maps[y][x] for y,x in coords])
            values.rotate(1)
            for (y,x), value in zip(coords,values):
                maps[y][x]=value
    mins=min(mins,get_A(maps))
print(mins)