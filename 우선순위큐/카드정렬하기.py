import sys
sys.stdin = open('카드정렬하기_input.txt')
import heapq
n = int(input())
arr = []
ans = 0

for i in range(n) :
    x = int(input())
    heapq.heappush(arr,(x))
while arr :
    if len(arr) >= 2 :
        tmp1 = heapq.heappop(arr)
        tmp2 = heapq.heappop(arr)
        tmp = tmp1 + tmp2
        ans += tmp
        heapq.heappush(arr, (tmp))
    elif len(arr) == 1 :
        break

print(ans)