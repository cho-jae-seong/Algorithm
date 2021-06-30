from itertools import combinations
import sys

ja=['a','e','i','o','u']
l,c=map(int, sys.stdin.readline().split())
li=list(map(str, sys.stdin.readline().split()))
li.sort()
cb=list(combinations(li,l))
for i in cb:
    cnt=0
    for j in i:
        if j in ja:
            cnt+=1
    if cnt>=1 and cnt<=l-2:
        print("".join(i))
