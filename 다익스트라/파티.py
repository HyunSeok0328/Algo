import sys
sys.stdin = open('파티_input.txt')
import heapq
n,m,x = map(int,input().split())
arr = [[] for _ in range(n+1)]

inf = float('inf')
for _ in range(m) :
    a,b ,cost = map(int,input().split())
    arr[a].append((b,cost))

def dijkstra(start) :
    q = []
    distance = [inf] * (n+1)

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue
        for node_index, node_cost in arr[now] :
            cost = dist + node_cost

            if distance[node_index] > cost :
                distance[node_index] = cost
                heapq.heappush(q,(cost,node_index))
    return distance

result = 0
for i in range(1,n+1) :
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result,go[x]+back[i])
print(result)