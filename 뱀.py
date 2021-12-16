import sys
sys.stdin = open('뱀_input.txt')
from collections import deque

def bfs() :
    global cnt
    d = 1
    nx = 0
    ny = 0
    while q :
        x,c = q.popleft()

        while cnt != int(x) :
            nx += dx[d]
            ny += dy[d]
            cnt += 1
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 :
                snake.append((nx, ny))
                arr[nx][ny] = 0
            elif (nx,ny) in snake :
                return cnt
                break
            elif 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0  :
                snake.append((nx,ny))
                snake.popleft()
            else :
                return cnt
                break
        if c == 'D':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4
    while True :
        nx += dx[d]
        ny += dy[d]
        cnt += 1
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
            snake.append((nx, ny))
            arr[nx][ny] = 0
        elif (nx, ny) in snake:
            return cnt
            break
        elif 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            snake.append((nx, ny))
            snake.popleft()

        else:
            return cnt
            break

cnt = 0
q= deque()
snake = deque()
N = int(input())
K = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = [[0] * N for _ in range(N)]
for _ in range(K) :
    x, y = map(int,input().split())
    arr[x-1][y-1] = 1
L = int(input())
for _ in range(L) :
    X, C = input().split()
    q.append((X,C))
snake.append((0,0))
bfs()
print(cnt)
