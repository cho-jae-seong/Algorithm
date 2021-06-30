from itertools import combinations
import sys

n,m=map(int, sys.stdin.readline().split())
chicken=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li=[]
for i in range(n):
    for j in range(n):
        if chicken[i][j]==2:
            li.append([i,j])
            chicken[i][j]=0
cb=list(combinations(li,m))
min_distance=sys.maxsize
for i in range(len(cb)):
    distance=0
    for p in range(n):
        for k in range(n):
            if chicken[p][k]==1:
                temp=sys.maxsize
                for j in range(m):
                    temp=min(temp, abs(p-cb[i][j][0])+abs(k-cb[i][j][1]))
                distance+=temp
    min_distance=min(min_distance,distance)
print(min_distance)