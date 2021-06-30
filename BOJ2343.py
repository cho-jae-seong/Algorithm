import sys

n,m=map(int, sys.stdin.readline().split())
lesson=list(map(int, sys.stdin.readline().split()))

l=max(lesson)
r=sum(lesson)
while l<=r:
    total=0
    cnt=0
    mid=(l+r)//2
    for i in range(n):
        if total+lesson[i]>mid:
            total=0
            cnt+=1
        total+=lesson[i]
    if total!=0:
        cnt+=1
    if cnt<=m:
        r=mid-1
    else:
        l=mid+1
print(l)
