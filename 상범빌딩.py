import sys
sys.stdin = open('상범빌딩_input.txt')
import sys

input = sys.stdin.readline
from collections import deque

def bfs(x,y,z) :
    q.append((x,y,z))
    while q :
        z,y,x = q.popleft()
        if arr[z][y][x] == 'E' :
            print(f'Escaped in {visit[z][y][x]} minute(s).')
            return
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L :
                if (arr[nz][ny][nx] == '.' or arr[nz][ny][nx] == 'E') and visit[nz][ny][nx] == 0 :
                    q.append((nz,ny,nx))
                    visit[nz][ny][nx] = visit[z][y][x] + 1
    print("Trapped!")

while True :
    q=deque()
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0 :
        break
    arr = [0] * L
    visit = [[[0] * C for _ in range(R) ] for _ in range(L)]

    for i in range(L) :
        arr[i] = [list(map(str,input())) for _ in range(R)]
        input()

    for i in range(L) :
        for j in range(R) :
            for k in range(C) :
                if arr[i][j][k] == 'S' :
                    bfs(i,j,k)