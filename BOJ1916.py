import sys
import heapq

def dijkstra(start,end):
    heap=[]
    heapq.heappush(heap,(0,start))
    distance=[sys.maxsize]*(n+1)
    distance[start]=0

    while heap:
        weight,index=heap.heappop(heap)
        for e,c in bus[index]:
            if distance[e]>weight+c:
                distance[e]=weight+c
                heapq.heappush(heap,(weight+c,e))
    return distance[end]

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
bus=[[]for _ in range(n+1)]
for _ in range(m):
    start,end,cost=map(int, sys.stdin.readline().split())
    bus[start].append((end,cost))
start,end=map(int,sys.stdin.readline().split())
print(dijkstra(start,end))


