import sys
from collections import Counter
from functools import reduce

def R(array):
    mx=0
    for i in range(len(array)):
        X=Counter(array[i])
        del X[0]
        X=list(X.items())
        X.sort(key=lambda x: (x[1],x[0]))
        if len(X)>50:
            X=X[:50]
        array[i]=reduce(lambda x, y: list(x)+list(y), X[1:], list(X[0]))
        mx=max(mx,len(array[i]))

    for i in range(len(array)):
        if len(array[i])<mx:
            array[i].extend([0]*(mx-len(array[i])))

r,c,k=map(int, sys.stdin.readline().split())
r,c=r-1,c-1
a=[list(map(int, sys.stdin.readline().split()))for _ in range(3)]
if r<len(a) and c<len(a[0]) and a[r][c]==k:
        print(0)
        exit(0)
time=0
while True:
    row_len=len(a)
    col_len=len(a[0])
    if row_len>=col_len:
        R(a)
    else:
        a=list(map(list, zip(*a)))
        R(a)
        a=list(map(list, zip(*a)))
    time+=1
    if time>100:
        print(-1)
        exit(0)
    if r<len(a) and c<len(a[0]) and a[r][c]==k:
        print(time)
        exit(0)
