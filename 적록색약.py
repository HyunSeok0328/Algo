import sys
sys.stdin = open('적록색약_input.txt')

from collections import deque

N = int(input())
arr = [list(map(str,input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
q = deque()
q2 = deque()
q3 = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
cnt2 = 0
def bfs() :
    global cnt
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and arr[nx][ny] == 'R':
                q.append((nx,ny))
                visit[nx][ny] = 1
    while q2 :
        x,y = q2.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and arr[nx][ny] == 'G':
                q2.append((nx,ny))
                visit[nx][ny] = 1
    while q3 :
        x,y = q3.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and arr[nx][ny] == 'B':
                q3.append((nx,ny))
                visit[nx][ny] = 1
    cnt += 1

def bfs2() :
    global cnt2
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and (arr[nx][ny] == 'R' or arr[nx][ny] == 'G'):
                q.append((nx,ny))
                visit[nx][ny] = 1
    while q3 :
        x,y = q3.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and arr[nx][ny] == 'B':
                q3.append((nx,ny))
                visit[nx][ny] = 1
    cnt2 += 1



for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 'R' and visit[i][j] == 0 :
            q.append((i,j))
            visit[i][j] = 1
            bfs()
        elif arr[i][j] == 'G' and visit[i][j] == 0 :
            q2.append((i,j))
            visit[i][j] = 1
            bfs()
        elif arr[i][j] == 'B' and visit[i][j] == 0 :
            q3.append((i,j))
            visit[i][j] = 1
            bfs()

visit = [[0] * N for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 'R' and visit[i][j] == 0  :
            q.append((i,j))
            visit[i][j] = 1
            bfs2()
        elif arr[i][j] == 'G' and visit[i][j] == 0  :
            q.append((i,j))
            visit[i][j] = 1
            bfs2()

        elif arr[i][j] == 'B' and visit[i][j] == 0 :
            q3.append((i,j))
            visit[i][j] = 1
            bfs2()
print(f'{cnt} {cnt2}')
