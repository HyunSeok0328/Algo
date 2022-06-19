import sys
sys.stdin = open('테트로미노_input.txt')


def dfs(x,y,cnt,total) :
    global ans
    if ans >= total + max_value * (3 - cnt):
        return
    if cnt == 3 :
        ans = max(ans,total)
        return
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 :
            if cnt == 1 :
                visit[nx][ny] = 1
                dfs(x,y,cnt+1,total + arr[nx][ny])
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(nx,ny,cnt+1,total + arr[nx][ny])
            visit[nx][ny] = 0
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
max_value = max(map(max, arr))
for i in range(N) :
    for j in range(M) :
        visit[i][j] = 1
        dfs(i,j,0,arr[i][j])
        visit[i][j] = 0
print(ans)