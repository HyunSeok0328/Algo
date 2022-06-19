import sys
sys.stdin = open('벽부수고탈출하기_input.txt')
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int,input())) for _ in range(n)]


visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
q.append((0,0,0))

def bfs() :

    while q :

        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return visit[x][y][z]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                # 파괴 햇을경우
                if arr[nx][ny] == 1 and z == 0 :
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    q.append((nx,ny,1))
                elif arr[nx][ny] == 0 and visit[nx][ny][z] == 0 :
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    q.append((nx,ny,z))
    return -1

print(bfs())
