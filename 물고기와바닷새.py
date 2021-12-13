import sys
sys.stdin = open('물고기와바닷새_input.txt')

from collections import deque
T = int(input())
dy = [-1,1]

def solve(a,b,ans) :
    global answer
    visit[a][b] = 1
    while whale :
        x,y = whale.popleft()
        nx = x+1
        if 0<= nx < R :
            arr[nx][y] = 0
            whale.append((nx,y))
    for i in range(2) :
        ny = b + dy[i]
        if 0 <= a < R and 0 <= ny < C and visit[a][ny] == 0:
            if arr[a][ny] == 1:
                visit[a][ny] = 1
                recommend.append(ans+2)
                solve(a,ny,ans+2)
                visit[a][ny] = 0
            else :
                visit[a][ny] = 1
                solve(a,ny,ans+1)
                visit[a][ny] = 0
    # while q :
    #     a,b = q.popleft()
    #     for i in range(2) :
    #         ny = b + dy[i]
    #         if 0<= a <R and 0<= ny <C and visit[a][ny] == 0 :
    #             if arr[a][ny] == 1 :
    #                 visit[a][ny] = 1
    #                 ans += 2
    #                 a += 1
    #                 q.append((a,ny))
    #                 break
    #             else :
    #                 visit[a][ny] = 1
    #                 ans += 1
    #                 q.append((a,ny))




for tc in range(1,T+1) :
    R,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(R)]
    visit = [[0] * C for _ in range(R)]
    ans = 0
    q = deque()
    whale = deque()
    recommend = []
    answer = 987654321
    for i in range(R) :
        for j in range(C) :
           if arr[i][j] == 2 :
                whale.append((i,j))
    solve(0,0,0)
    print(recommend)
