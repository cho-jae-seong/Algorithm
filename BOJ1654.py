import sys

k,n=map(int, sys.stdin.readline().split())
line=[]
for i in range(k):
    a=int(input())
    line.append(a)
maximum=max(line)
l=1
r=maximum
while l<=r:
    mid=(l+r)//2
    sum=0
    for i in line:
        sum+=i//mid
    if sum<n:
        r=mid-1
    else:
        answer=mid
        l=mid+1
print(answer)