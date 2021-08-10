import sys

def check(mid):
    max_s=min_s=score[0]
    cnt=1
    for i in range(1,n):
        max_s=max(max_s,score[i])
        min_s=min(min_s,score[i])
        if max_s-min_s>mid:
            cnt+=1
            max_s=score[i]
            min_s=score[i]
    return cnt

n,m=map(int, sys.stdin.readline().split())
score=list(map(int, sys.stdin.readline().split()))

l=0
r=max(score)
answer=0
while l<=r:
    mid=(l+r)//2
    if check(mid)<=m:
        r=mid-1
        answer=mid
    else:
        l=mid+1
print(answer)