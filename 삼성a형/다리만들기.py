import sys
sys.stdin = open('다리만들기_input.txt')
from collections import deque

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = float('inf')
k = 1
def bfs() :
    while q :
        x, y, z = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visit[nx][ny] == 0 :
                q.append((nx,ny,z))
                arr[nx][ny] = z
                visit[nx][ny] = 1
def bfs2(num):
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if visit[nx][ny] == 1 and arr[nx][ny] != num :
                    return c2[x][y]-1
                if visit[nx][ny] == 0 and c2[nx][ny] == 0 :
                    c2[nx][ny] = c2[x][y] + 1
                    q.append((nx,ny))


for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1 and visit[i][j] == 0 :
            arr[i][j] = k
            visit[i][j] = 1
            q.append((i,j,k))

            bfs()
            k += 1

for r in range(1,k) :
    q = deque()
    c2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N) :
            if arr[i][j] == r and visit[i][j] == 1 :
                q.append((i,j))
                c2[i][j] = 1

    res = bfs2(r)
    ans = min(ans,res)
print(ans)

