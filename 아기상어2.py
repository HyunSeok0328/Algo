import sys
sys.stdin = open('아기상어2_input.txt')

from collections import deque
def bfs() :
    global ans
    while q :
        x,y = q.popleft()
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 :
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
q= deque()
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
ans = 0

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            q.append((i,j))
            visit[i][j] = 1
bfs()
print(max(map(max,visit))-1)
