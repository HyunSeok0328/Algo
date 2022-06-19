import sys
sys.stdin = open('파이프옮기기_input.txt')

def dfs(x,y,z) :
    global cnt
    if x == N-1 and y == N-1 :
        cnt += 1
        return
    if x + 1 < N and y + 1 < N:
        if arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0:
            dfs(x+1,y+1,2)
    if z == 0 or z== 2 :
        if y+1 < N :
            if arr[x][y+1] == 0 :
                dfs(x,y+1,0)
    if z == 1 or z == 2 :
        if x+1 < N :
            if arr[x+1][y] == 0 :
                dfs(x+1,y,1)

cnt = 0
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dfs(0,1,0)
print(cnt)