import sys
sys.stdin = open('카드정렬하기_input.txt')
import heapq

N = int(input())
arr = []
for i in range(N) :
    heapq.heappush(arr, int(input()))
if len(arr) == 1:
    print(0)
else :
    ans = 0
    while len(arr) > 1 :
        temp = heapq.heappop(arr)
        temp2 = heapq.heappop(arr)
        ans += temp + temp2
        heapq.heappush(arr, temp + temp2)

    print(ans)