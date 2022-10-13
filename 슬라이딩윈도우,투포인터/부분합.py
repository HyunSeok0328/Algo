import sys
sys.stdin = open('부분합_input.txt')

n, s = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
ans = 100001
value = 0
left, right = 0 , 0
while True :
    if value >= s :
        ans = min(right - left, ans)
        value -= arr[left]
        left += 1

    elif right == n :
        break
    else :
        value += arr[right]
        right += 1
if ans == 100001 :
    ans = 0
print(ans)