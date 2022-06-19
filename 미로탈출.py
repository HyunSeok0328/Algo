import sys
sys.stdin = open('미로탈출_input.txt')

from collections import deque
N,M = map(int,input().split())
Hx, Hy = map(int,input().split())
Ex, Ey = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

q = deque()
q.append((Hx-1,Hy-1,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs() :
    while q :
        x,y,z = q.popleft()
        if x == Ex-1 and y == Ey-1 :
            return visit[x][y][z]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if arr[nx][ny] == 1 and z == 0 :
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    q.append((nx,ny,1))
                elif arr[nx][ny] == 0 and visit[nx][ny][z] == 0 :
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    q.append((nx,ny,z))
    return -1
print(bfs())