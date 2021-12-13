import sys

sys.stdin = open('꽃길_input.txt')
def dfs(cost, cnt) :
    global ans
    if cnt == 3 :
        ans = min(ans, cost)
        return
    for i in range(1, N-1) :
        for j in range(1, N-1) :
            if check(i,j) == 1 :
                for k in range(5) :
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visit[nx][ny] = 1
                dfs(cost + cal(i,j), cnt+1)
                for l in range(5) :
                    nx = i + dx[l]
                    ny = j + dy[l]
                    visit[nx][ny] = 0
def check(x,y) :
    global N
    for k in range(5) :
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 > ny or ny> N-1 or 0> nx or nx > N-1 or visit[nx][ny] == 1:
            return 0

    return 1


def cal(x,y) :
    result = 0
    for k in range(5) :
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N :
            result += arr[nx][ny]
        else :
            return
    return result


ans = 987654312
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
visit = [[0] * N for _ in range(N)]
dfs(0,0)
print(ans)
