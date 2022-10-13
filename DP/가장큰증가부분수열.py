import sys
sys.stdin = open('가장큰증가부분수열_input.txt')

n = int(input())
arr = list(map(int,input().split()))
dp = [0] * (n+1)
dp[0] = arr[0]
for i in range(1,n) :
    for j in range(i) :
        if arr[j] < arr[i] :
            dp[i] = max(dp[i],arr[i]+dp[j])
        else :
            dp[i] = max(dp[i],arr[i])
print(max(dp))

