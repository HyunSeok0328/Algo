import sys
sys.stdin = open('불_input.txt')

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs() :
    while q2 :
        x,y = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and fire[nx][ny] == 0 :
                if arr[nx][ny] == '.' :
                    q2.append((nx,ny))
                    fire[nx][ny] = fire[x][y] + 1
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 :
                if fire[nx][ny] == 0 or fire[nx][ny] > (visit[x][y] + 1) :
                    if arr[nx][ny] == '.' :
                        q.append((nx,ny))
                        visit[nx][ny] = visit[x][y] + 1
            if (nx == h or nx == -1) or (ny == w or ny == -1) :
                print(visit[x][y])
                return
    print('IMPOSSIBLE')

w, h = map(int,input().split())
arr = [list(map(str,input())) for _ in range(h)]
visit = [[0] * w for _ in range(h)]
fire = [[0] * w for _ in range(h)]
q = deque()
q2 = deque()

for i in range(h) :
    for j in range(w) :
        if arr[i][j] == 'F' :
            q.append((i,j))
            visit[i][j] = 1
        elif arr[i][j] == 'J' :
            q2.append((i,j))
            fire[i][j] = 1
bfs()

