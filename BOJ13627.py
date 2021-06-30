import sys

n,r = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
if n==r:
    print('*')
else:
    for i in range(1,n+1):
        if i not in arr:
            print(i,end=' ')