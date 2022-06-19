import sys
sys.stdin = open('dfs와bfs_input.txt')
from collections import deque
N, M , V = map(int,input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)
q = deque()

for i in range(M) :
    a, b = map(int,input().split())
    arr[a][b] = arr[b][a] = 1

def dfs(V) :
    visit[V] = 1

    print(V, end=' ')

    for i in range(1,N+1) :
        if visit[i] == 0 and arr[V][i] == 1 :
            dfs(i)

def bfs(V) :
    q = [V]
    visit[V] = 0
    while q :
        V = q.pop(0)
        print(V, end = ' ')
        for i in range(1,N+1) :
            if(visit[i]==1 and arr[V][i] == 1) :
                q.append(i)
                visit[i] = 0

dfs(V)
print()
bfs(V)


