import sys

sys.stdin = open('미로탐색_input.txt')

from collections import deque

def dfs(x,y,cnt) :
    global N,M,ans
    if cnt >= ans :
        return
    if x == N-1 and y == M-1 :
        ans = min(ans,cnt)
        return
    for i in range(4) :
        if arr[x][y] == 1 :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<= ny < M and visit[nx][ny] == 0 :
                visit[nx][ny] = 1
                dfs(nx,ny,cnt+1)
                visit[nx][ny] = 0

def bfs() :
    while q:
        x,y = q.popleft()
        if x == N - 1 and y == M - 1 :
            return visit[x][y]
        for i in range(4) :
            if arr[x][y] == 1 :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))
cnt = 0
ans = 987654321
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
q.append((0,0))

print(bfs()+1)
