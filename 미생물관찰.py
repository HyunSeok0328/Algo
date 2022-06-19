import sys
sys.stdin = open('미생물관찰_input.txt')

from collections import deque

def bfs() :
    while q :
        global maxnumber,acnt,numberarr
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny <M and visit[nx][ny] == 0 :
                if arr[nx][ny] == 'A' :
                    visit[nx][ny] = 1
                    maxnumber += 1
                    q.append((nx,ny))
    acnt += 1
    numberarr.append(maxnumber)
    maxnumber = 1
def bfs2() :
    while q2 :
        global maxnumber, bcnt, nubmerarr
        x,y = q2.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny <M and visit[nx][ny] == 0:
                if arr[nx][ny] == 'B' :
                    visit[nx][ny] = 1
                    maxnumber += 1
                    q2.append((nx,ny))
    bcnt += 1
    numberarr.append(maxnumber)
    maxnumber = 1


T = int(input())
for tc in range(1,T+1) :
    numberarr = []
    maxnumber = 1
    acnt = 0
    bcnt = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q2 = deque()
    N, M = map(int,input().split())
    visit = [[0] * M for _ in range(N)]
    arr = [list(map(str,input())) for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] == 'A' and visit[i][j] == 0:
                visit[i][j] = 1
                q.append((i,j))
                bfs()
            elif arr[i][j] == 'B' and visit[i][j] == 0 :
                visit[i][j] = 1
                q2.append((i,j))
                bfs2()

    print(f'#{tc} {acnt} {bcnt} {max(numberarr)}')