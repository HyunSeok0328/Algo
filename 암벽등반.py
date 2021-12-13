import sys

sys.stdin = open('암벽등반_input.txt')

dx=[-1,1,0,0]
dy=[0,0,-1,1]
T = int(input())

def dfs(x,y,cnt,ans) :
    global L,dap,c_ans
    if cnt == 0 :
        c_ans.append((x,y))
        return
    if ans > dap :
        return
    if len(c_ans) >= 10000 :
        return
    for i in range(4) :
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0<= nx < M and 0<= ny < N and visit[nx][ny] == 0 :
            if arr[nx][ny] == 3 :
                answer.append(ans)
                dap = min(dap,ans)
                return
            elif arr[nx][ny] == 1 :
                visit[nx][ny] = 1
                ans += 1
                dfs(nx,ny,L,ans)
                ans -= 1
                dfs(nx, ny, cnt - 1,ans)
                visit[nx][ny] = 0
            else :
                visit[nx][ny] = 1
                dfs(nx,ny,cnt-1,ans)
                visit[nx][ny] = 0




for tc in range(1,T+1) :
    M,N,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]
    visit = [[0] * N for _ in range(M)]
    ans = 0
    answer = []
    c_ans = []
    dap = 987654321
    for i in range(M) :
        for j in range(N) :
            if arr[i][j] == 2 :
                dfs(i,j,L,ans)
    if answer :
        print(f'#{tc} {dap}')
    else :
        print(f'#{tc} -1')