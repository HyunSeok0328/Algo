import sys
sys.stdin = open('1,2,3더하기4_input.txt')

t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])