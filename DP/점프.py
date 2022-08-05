import sys
sys.stdin = open('점프_input.txt')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == y == N-1:
            print(dp[x][y])
            break

        jump = arr[x][y]
        if x + jump < N:
            dp[x + jump][y] += dp[x][y]
        if y + jump < N:
            dp[x][y + jump] += dp[x][y]

