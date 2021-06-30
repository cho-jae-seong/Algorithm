import sys

h,w=map(int,sys.stdin.readline().split())
rain=list(map(int, sys.stdin.readline().split()))
total=0
for i in range(1,w-1):
    maximum1=max(rain[:i])
    maximum2=max(rain[i+1:])
    minimum=min(maximum1,maximum2)
    if minimum>rain[i]:
        total+=minimum-rain[i]
print(total)