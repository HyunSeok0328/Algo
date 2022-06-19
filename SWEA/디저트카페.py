import sys
sys.stdin = open('디저트카페_input.txt')


def dfs(x,y,cnt,visited) :
    global ans
    if cnt == 4 :
        return
    if fx == x and fy == y and len(visited) != 0 :
        ans = max(len(visited),ans)

    if 0 <= x < N and 0<= y < N :
        if arr[x][y] in visited :
            return
        dfs(nx, ny, cnt, visited + [arr[nx][ny]])
        dfs(nx, ny, cnt + 1, visited + [arr[nx][ny]])




T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    visit = [[0] * N for _ in range(N)]
    ans = -1
    for i in range(N) :
        for j in range(N) :
            fx , fy = i,j
            dfs(i,j,0,[arr[i][j]])
    print(f'#{tc} {ans}')