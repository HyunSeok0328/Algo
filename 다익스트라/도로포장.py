import sys
sys.stdin = open('도로포장_input.txt')
import heapq

n,m,k = map(int,input().split())
arr = [[] for _ in range(n+1)]
INF = float('inf')
distance = [[INF for _ in range(k+1)] for _ in range(n+1)]

for _ in range(m) :
    a,b,cost = map(int,input().split())
    arr[a].append((cost,b))
    arr[b].append((cost,a))

def dijkstra(start) :
    q = []
    cnt = 0
    distance[start][cnt] = 0
    heapq.heappush(q,(0,start,cnt))

    while q :
        dist, now, cnt= heapq.heappop(q)
        if distance[now][cnt] < dist :
            continue
        for node_cost,node_index in arr[now] :
            cost = dist + node_cost
            if distance[node_index][cnt] > cost :
                distance[node_index][cnt] = cost
                heapq.heappush(q,(cost,node_index,cnt))

            if cnt < k and distance[node_index][cnt+1] > dist :
                distance[node_index][cnt+1] = dist
                heapq.heappush(q, (dist, node_index, cnt+1))
dijkstra(1)
print(min(distance[n]))

