import sys

button = {str(i) for i in range(10)}

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
if m!=0:
    button-=set(map(str, sys.stdin.readline().split()))
min_cnt=abs(100-n)

for num in range(1000001):
    num=str(num)
    for j in range(len(num)):
        if num[j] not in button:
            break
        elif j==len(num)-1:
            min_cnt=min(min_cnt,abs(n-int(num))+len(str(num)))
print(min_cnt)
