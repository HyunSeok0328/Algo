import sys
sys.stdin = open('단지번호붙이기_input.txt')

from collections import deque

def bfs(cnt) :
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visit[nx][ny] == 0 :
                visit[nx][ny] = 1
                q.append((nx,ny))
                arr[nx][ny] = cnt

q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1 and visit[i][j] == 0 :
            q.append((i,j))
            cnt += 1
            arr[i][j] = cnt
            visit[i][j] = 1
            bfs(cnt)
x = []
newarr = []
print(cnt)
for i in range(1, cnt+1) :
    x = 0
    for j in range(N) :
        x += arr[j].count(i)
    newarr.append(x)
newarr.sort()
for i in newarr :
    print(i)
