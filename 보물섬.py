import sys
sys.stdin = open('보물섬_input.txt')

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

cnt = 0
q=deque()

def bfs() :
    global cnt
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C :
                if arr[nx][ny] == 'L' and visit[nx][ny] == 0 :
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1
                    cnt = max(cnt, visit[nx][ny])


for i in range(R) :
    for j in range(C) :
        if arr[i][j] == 'L' :
            q.append((i,j))
            visit = [[0] * C for _ in range(R)]
            visit[i][j] = 1
            bfs()

print(cnt-1)
