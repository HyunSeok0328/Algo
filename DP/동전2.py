import sys
sys.stdin = open('동전2_input.txt')

n, k = map(int,input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))
dp = [10001] * (k+1)
dp[0] = 0
for i in range(1, k + 1):
    for j in arr :
        if i < j: continue
        dp[i] = min(dp[i], dp[i - j] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])