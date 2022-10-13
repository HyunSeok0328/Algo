import sys
sys.stdin = open('ATM_input.txt')

N = int(input())
arr = list(map(int,input().split()))
ans = 0
arr.sort()
ans2 = 0
for i in range(len(arr)) :
    ans += arr[i]
    ans2 += ans
print(ans2)