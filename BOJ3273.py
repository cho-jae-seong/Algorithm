import sys

n=int(sys.stdin.readline().strip())
number=list(map(int, sys.stdin.readline().split()))
x=int(sys.stdin.readline().strip())
number.sort()
left,right=0,n-1
answer=0
while left<right:
    tmp=number[left]+number[right]
    if tmp==x:
        answer+=1
    if tmp<x:
        left+=1
        continue
    right-=1
print(answer)