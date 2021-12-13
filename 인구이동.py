import sys
sys.stdin = open('인구이동_input.txt')
from collections import deque

def bfs(x,y) :
    global is_move
    q = deque()
    stack = []
    q.append((x,y))
    stack.append((x,y))
    visit[x][y] = 1
    value = arr[x][y]
    cnt = 1
    while q :
        a,b = q.popleft()
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 :
                if L <= abs(arr[a][b] - arr[nx][ny]) <= R :
                    q.append((nx,ny))
                    stack.append((nx,ny))
                    value += arr[nx][ny]
                    cnt += 1
                    visit[nx][ny] = 1
    if cnt > 1 :
        is_move = True
        for nx, ny in stack :
            arr[nx][ny] = value//cnt



N, L, R = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
is_move = False
while True :
    is_move = False
    visit = [[0] * N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if visit[i][j] == 0 :
                bfs(i,j)
    if is_move :
        ans += 1
    else :
        break
print(ans)
