import sys
sys.stdin = open('감시_input.txt')

def solution(n) :
    global ans
    if n == C :
        cnt = 0
        for i in range(N) :
            for j in range(M) :
                if arr[i][j] == 0 :
                    cnt += 1
        ans = min(ans,cnt)
        return
    a, b, c = cctvs[n]
    for i in check[c] :
        watch = []
        for j in i :
            nx, ny = a,b
            while 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 6:
                if arr[nx][ny] == 0 :
                    watch.append((nx,ny))
                    arr[nx][ny] = -1
                nx += dx[j]
                ny += dy[j]
        solution(n+1)
        for k in watch :
            arr[k[0]][k[1]] = 0


N,M = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(N)]
check = [[[0],[1],[2],[3]],
        [[0,2],[1,3]],
        [[0,1],[1,2],[2,3],[3,0]],
        [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
        [[0,1,2,3]]]
cctvs = []
for i in range(N) :
    for j in range(M) :
        if 1 <= arr[i][j] < 6 :
            cctvs.append((i,j, arr[i][j]-1))
C = len(cctvs)
ans = N*M
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
solution(0)
print(ans)
