import sys
sys.stdin = open('제곱수의합_input.txt')

n = int(input())
dp = [x for x in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,i) :
        if i < j*j :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])