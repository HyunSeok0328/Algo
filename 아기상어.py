import heapq
import sys
sys.stdin = open('아기상어_input.txt')

from collections import deque


def bfs(a,b) :
    while True :
        global size,ans,stack
        q = deque()
        q.append((a,b,0))
        visit = [[0] * n for _ in range(n)]
        visit[a][b] = 1
        fish = []
        flag = float('inf')
        while q :
            x,y,cnt = q.popleft()
            if cnt > flag :
                break
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] <= size:
                    if 0 < arr[nx][ny] < size :
                        heapq.heappush(fish, (nx,ny,cnt + 1))
                        flag = cnt
                    q.append((nx, ny, cnt + 1))
                    visit[nx][ny] = 1

        if len(fish) > 0 :
            a,b,move = heapq.heappop(fish)
            ans += move
            stack += 1
            arr[a][b] = 0
            if stack == size :
                size += 1
                stack = 0
        else :
            break





n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
size = 2
cnt = 0
stack = 0
ans = 0

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 9 :
            arr[i][j] = 0
            bfs(i,j)
            break
print(ans)
