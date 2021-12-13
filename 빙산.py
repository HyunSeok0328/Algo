import sys

sys.stdin = open('빙산_input.txt')
from collections import deque
import copy
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
qtmp = deque()
cnt = 0
chk = 0
ans = 0

def chkice(c_matrix):
    count = 0
    for y in range(1, N-1):
        for x in range(1, M-1):
            if c_matrix[y][x]:
                count += 1
                c_matrix[y][x] = 0
                q.append((y, x))
                qtmp.append((y, x))
                while q:
                    a, b = q.popleft()
                    for i in range(4):
                        ny = a + dy[i]
                        nx = b + dx[i]
                        if c_matrix[ny][nx] != 0:
                            q.append((ny, nx))
                            qtmp.append((ny, nx))
                            c_matrix[ny][nx] = 0
    return count
def bfs() :
    global cnt
    newarr = copy.deepcopy(arr)
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0<= ny < M and visit[nx][ny] == 0 :
                if newarr[nx][ny] == 0 :
                    arr[x][y] -= 1
                    if arr[x][y] <= 0 :
                        arr[x][y] = 0

while True:
    matrix2 = copy.deepcopy(arr)
    chk = chkice(matrix2)
    if chk == 0:
        ans = 0
        break
    elif chk > 1:
        break
    ans += 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                q.append((i, j))
    bfs()
print(ans)
