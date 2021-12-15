import sys
sys.stdin = open('섬의개수_input.txt')

from collections import deque
def bfs() :
    global cnt
    while q:
        x,y = q.popleft()
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and arr[nx][ny] == 1 :
                visit[nx][ny] = 1
                q.append((nx,ny))
    cnt += 1
while True :
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    cnt = 0
    w, h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    q = deque()
    visit = [[0] * w for _ in range(h)]
    for i in range(h) :
        for j in range(w) :
            if arr[i][j] == 1 and visit[i][j] == 0:
                visit[i][j] = 1
                q.append((i,j))
                bfs()
    print(cnt)



