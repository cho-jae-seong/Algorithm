from itertools import combinations
import sys

answer=0
n,s=map(int, sys.stdin.readline().split())
li=list(map(int, sys.stdin.readline().split()))
for i in range(1,n+1):
    cb=list(combinations(li,i))
    for j in cb:
        if sum(j)==s:
            answer+=1
print(answer)