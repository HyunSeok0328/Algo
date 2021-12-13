import sys
sys.stdin = open('안전영역_input.txt')
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs() :
    global cnt,ans
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 :
                visit[nx][ny] = 1
                q.append((nx,ny))
    cnt += 1

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

q = deque()
tmp = 0
ans = 0
for i in range(N) :
    for j in range(N) :
        if arr[i][j] > tmp :
            tmp = arr[i][j]
for k in range(tmp+1) :
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] <= k :
                visit[i][j] = 1
    for x in range(N) :
        for y in range(N) :
            if visit[x][y] == 0  :
                visit[x][y] = 1
                q.append((x,y))
                bfs()
            if cnt > ans:
                ans = cnt

print(ans)

