import sys
sys.stdin =open('마법사상어와비바라기_input.txt')

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]
clouds = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]
for i in range(m) :
    next_cloud = []
    d,s = map(int,input().split())
    for x,y in clouds :
        nx = (n + x + (dx[d])*s) % n
        ny = (n + y + (dy[d])*s) % n
        next_cloud.append((nx,ny))

    visit = [[0] * n for _ in range(n)]
    for x,y in next_cloud :
        arr[x][y] += 1
        visit[x][y] = 1

    clouds = []

    cx = [-1,-1,1,1]
    cy = [-1,1,-1,1]
    for x,y in next_cloud :
        cnt = 0
        for i in range(4) :
            nx = x + cx[i]
            ny = y + cy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] >= 1 :
                cnt += 1
        arr[x][y] += cnt


    for i in range(n) :
        for j in range(n) :
            if arr[i][j] >= 2 and visit[i][j] == 0 :
                arr[i][j] -= 2
                clouds.append((i,j))

ans = 0
for i in range(n) :
    ans += sum(arr[i])
print(ans)