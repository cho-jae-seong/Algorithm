from collections import deque

N, K = map(int, input().split())
MAX_SIZE = 100001

q = deque()
q.append(N)

cnt=0
check=[-1]* MAX_SIZE
check[N]=0
while q:
    x = q.popleft()
    if x==K:
        cnt+=1
    for y in [x * 2, x + 1, x - 1]:
        if 0 <= y < MAX_SIZE:
            if check[y]==-1 or check[y]>=check[x]+1: 
                check[y]=check[x]+1
                q.append(y)

print(check[K])
print(cnt)






