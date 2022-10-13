import sys
sys.stdin = open('치즈_input.txt')
from collections import deque

def bfs() :
    cnt = 0
    q = deque()
    q.append((0,0))
    visit[0][0] = 1
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 :
                if arr[nx][ny] == 0 :
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                elif arr[nx][ny] == 1 :
                    arr[nx][ny] = 0
                    visit[nx][ny] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt




dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = []
n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

q = deque()

time = 0
while 1:
    time +=1
    visit = [[0]*m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(ans[-2])

