import sys
sys.stdin = open('가장긴감소하는부분수열_input.txt')

n = int(input())
arr = list(map(int,input().split()))

dp = [1] * n

for i in range(n) :
    for j in range(i) :
        if arr[i] < arr[j] :
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))