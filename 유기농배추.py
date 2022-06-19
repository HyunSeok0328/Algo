import sys
sys.stdin = open('유기농배추_input.txt')

from collections import deque

def bfs() :
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N :
                if arr[nx][ny] == 1 and visit[nx][ny] == 0 :
                    q.append((nx,ny))
                    visit[nx][ny] = 1
    global cnt
    cnt += 1



T = int(input())
for tc in range(1, T+1) :
    M, N, K = map(int,input().split())

    arr = [[0] * N for _ in range(M)]
    visit = [[0] * N for _ in range(M)]
    for i in range(K) :
        x , y = map(int, input().split())
        arr[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    q = deque()
    for i in range(M) :
        for j in range(N) :
            if arr[i][j] == 1 and visit[i][j] == 0:
                q.append((i,j))
                bfs()

    print(cnt)
