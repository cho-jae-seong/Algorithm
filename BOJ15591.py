import sys
from collections import defaultdict

N, Q = map(int,sys.stdin.readline().split())
USADO = defaultdict(list)
for _ in range(N-1):
    p, q, r = map(int,sys.stdin.readline().split())
    USADO[p].append([q,r])
    USADO[q].append([p,r])

def dfs(start, k):
    visited = [False for _ in range(N+1)]
    stack = [[start,float("INF")]]
    count = 0
    while stack:
        now_node, now_dis = stack.pop()
        if not visited[now_node] and now_dis >= k:
            stack.extend(USADO[now_node])
            visited[now_node] = True
            count += 1
    return count-1

for _ in range(Q):
    k, v = map(int,sys.stdin.readline().split())
    print(dfs(v,k))