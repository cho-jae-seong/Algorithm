import sys

n,s=map(int, sys.stdin.readline().split())
num=list(map(int, sys.stdin.readline().split()))
left,right,total,cnt=0,0,0,0
result=n
flag=False
while True:
    if total>=s:
        flag=True
        result=min(result,cnt)
        total-=num[left]
        left+=1
        cnt-=1
    elif right==n:
        break
    else:
        total+=num[right]
        right+=1
        cnt+=1

if flag:
    print(result)
else:
    print(0)