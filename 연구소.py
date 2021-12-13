
import sys
sys.stdin = open('연구소_input.txt')
import copy
from collections import deque
def bfs() :
    global ans
    newarr = copy.deepcopy(arr)
    for i in range(N) :
        for j in range(M) :
            if newarr[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if newarr[nx][ny] == 0 :
                    newarr[nx][ny] = 2
                    q.append((nx,ny))
    cnt = 0
    for i in newarr :
        cnt += i.count(0)
    ans = max(ans, cnt)

def wall(start, cnt) :
    if cnt == 3:
        bfs()
        return
    for i in range(start,N*M) :
        x = i // M
        y = i % M

        if arr[x][y] == 0 :
            arr[x][y] = 1
            wall(i+1 , cnt+1)
            arr[x][y] = 0

N,M = map(int,input().split())
ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = [list(map(int,input().split())) for _ in range(N)]
q = deque()
wall(0,0)
print(ans)
