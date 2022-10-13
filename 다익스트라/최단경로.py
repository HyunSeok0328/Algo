import sys
sys.stdin =open('최단경로_input.txt')

import heapq

v,e = map(int,input().split())
k = int(input())
inf = float('inf')
arr = [[ ] * (v+1) for _ in range(v+1)]
dis = [inf] * (v+1)
for _ in range(e) :
    a, b, c = map(int,input().split())
    arr[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if dis[now] < dist :
            continue
        for i in arr[now] :
            cost = dist + i[1]

            if cost < dis[i[0]] :
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(k)

for i in range(1,v+1) :
    if dis[i] == inf :
        print('INF')
    else :
        print(dis[i])