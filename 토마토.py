import sys
sys.stdin = open('토마토_input.txt')

from collections import deque

def bfs() :
    while q :
        a,b = q.popleft()
        for i in range(4) :
            nx = a+dx[i]
            ny = b+dy[i]
            if 0 <= ny < M and 0 <= nx < N and arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = arr[a][b] + 1


M, N = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
q=deque()
mode = 1
dy = [1,-1,0,0]
dx = [0,0,1,-1]
x = 0
y = 0
res =0
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1:
            q.append((i, j))
bfs()
for i in arr :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    if res < max(i) :
        res = max(i)
if mode == 1 :
    print(res-1)


