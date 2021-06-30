import sys

n = int(sys.stdin.readline())
arr = []
ans = sys.maxsize
for i in range(n):
    high = int(sys.stdin.readline().rstrip())
    arr.append(high)
for i in range(0,100-17):
    tempans = 0
    for j in range(0,n):
        if arr[j] < i:
            tempans+=(i-arr[j])*(i-arr[j])
        if arr[j] > i+17:
            tempans += (arr[j]-i-17)*(arr[j]-i-17)
    ans = min(ans,tempans)
print(ans)