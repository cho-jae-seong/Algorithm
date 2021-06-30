import sys
import heapq
from collections import defaultdict

def topologySort():
    result=[0 for i in range(n+1)]
    heap=[]
    for i in range(1,n+1):
        if indegree[i]==0:
            heapq.heappush(heap,i)
    for i in range(1,n+1):
        x=heapq.heappop(heap)
        result[i]=x
        for i in range(0,len(arr[x])):
            y=arr[x][i]
            indegree[y]-=1
            if indegree[y]==0:
                heapq.heappush(heap,y)
    for i in range(1,n+1):
        print('%d'%result[i],end=" ")


n,m=map(int, sys.stdin.readline().split())
arr=defaultdict(list)
indegree=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    arr[a].append(b)
    indegree[b]+=1
topologySort()