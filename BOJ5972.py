import sys
import heapq

def dijkstra(start,end):
    heap=[]
    heapq.heappush(heap,(0,start))
    distance=[sys.maxsize]*(n+1)
    distance[start]=0
    while heap:
        weight,index=heapq.heappop(heap)
        for e,c in graph[index]:
            if distance[e]>weight+c:
                distance[e]=weight+c
                heapq.heappush(heap,(weight+c,e))
    return distance[end]


n,m=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
print(dijkstra(1,n))
