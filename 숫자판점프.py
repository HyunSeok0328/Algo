import sys
sys.stdin = open('숫자판점프_input.txt')

def dfs(x,y,cnt,ans) :
    if cnt == 6 :
        dap.add(ans)
        return
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            visit[nx][ny] = 1
            dfs(nx,ny,cnt+1,ans + str(arr[nx][ny]))
            visit[nx][ny] = 0


arr = [list(map(int,input().split())) for _ in range(5)]
visit = [[0] * 5 for _ in range(5)]
ans = ''
dap = set()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(5) :
    for j in range(5) :
        dfs(i,j,0,'')
print(len(dap))