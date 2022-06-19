import sys
sys.stdin = open('벽부수고이동하기2_input.txt')

from collections import deque
chk = 0
def bfs() :
    global chk
    while q :
        x, y, z  = q.popleft()
        if x == n-1 and y == m-1 :
            print(visit[x][y][z])
            return
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if arr[nx][ny] == 0  and visit[nx][ny][z] == 0  :
                    q.append((nx,ny,z))
                    visit[nx][ny][z] = visit[x][y][z] + 1
                elif arr[nx][ny] == 1  :
                    if z < k and visit[nx][ny][z+1] == 0:
                        visit[nx][ny][z+1] = visit[x][y][z] + 1
                        q.append((nx,ny,z+1))
    print(-1)



n,m,k = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
visit = [[[0] * (k+1) for _ in range(m)]for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0,0))
visit[0][0][0] = 1
bfs()
