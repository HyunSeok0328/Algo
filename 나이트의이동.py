import sys
sys.stdin = open('나이트의이동_input.txt')

from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(sx,sy,fx,fy) :
    q = deque()
    q.append((sx,sy))
    while q :
        x,y = q.popleft()
        if x == fx and y == fy :
            return visit[x][y]
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I  :
                if visit[nx][ny] == 0 :
                    q.append((nx,ny))
                    visit[nx][ny] = visit[x][y] + 1


T = int(input())
for tc in range(1,T+1) :
    I = int(input())
    sx ,sy = map(int,input().split())
    fx ,fy = map(int,input().split())

    visit = [[0] * I for _ in range(I)]
    print(bfs(sx,sy,fx,fy))

