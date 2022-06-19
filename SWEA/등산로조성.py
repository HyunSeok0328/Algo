import sys
sys.stdin = open('등산로조성_input.txt')

def dfs(x,y,cnt,z) :
    global ans
    if cnt > ans :
        ans = max(cnt,ans)
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny][z] == 0 :
            if arr[x][y] <= arr[nx][ny] and z == 0:
                for i in range(1,K+1) :
                    arr[nx][ny] = arr[nx][ny] - i
                    dfs(x, y, cnt , 1)
                    arr[nx][ny] = arr[nx][ny] + i
            elif arr[x][y] > arr[nx][ny] :
                visit[nx][ny][z] = 1
                dfs(nx, ny, cnt + 1, z)
                visit[nx][ny][z] = 0



T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1,T+1) :
    ans = -1
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    maximum = max(map(max,arr))
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == maximum :
                visit[i][j][0] = 1
                dfs(i,j,1,0)
                visit[i][j][0] = 0

    print(f'#{tc} {ans}')