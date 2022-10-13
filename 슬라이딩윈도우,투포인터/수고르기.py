import sys
sys.stdin = open('수고르기_input.txt')
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
left, right = 0, 0
result = float('inf')

while left < N and right < N:
    if arr[right] - arr[left] <= M:
        right += 1
    else:
        result = min(result, arr[right] - arr[left])
        left += 1

print(result)
