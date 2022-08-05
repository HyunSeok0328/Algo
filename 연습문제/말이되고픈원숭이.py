import sys
sys.stdin = open('말이되고픈원숭이_input.txt')

from collections import deque

k = int(input())
w,h = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(h)]

cnt = 0
def bfs() :
    global cnt, k
    visit = [[[0] * 31 for _ in range(w)] for __ in range(h)]
    while q :
        x, y, z = q.popleft()
        if x == h-1 and y == w-1 :
            return visit[x][y][z]

        for j in range(4) :
            nx = x + dx2[j]
            ny = y + dy2[j]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 0 and visit[nx][ny][z] == 0 :
                q.append((nx,ny,z))
                visit[nx][ny][z] = visit[x][y][z] + 1
        if z > 0 :
            for i in range(8) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 0 and visit[nx][ny][z-1] == 0 :
                    q.append((nx,ny,z-1))
                    visit[nx][ny][z-1] = visit[x][y][z] + 1
    return -1



dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
dx2 = [-1,0,1,0]
dy2 = [0,1,0,-1]
q = deque()
q.append((0,0,k))
print(bfs())
