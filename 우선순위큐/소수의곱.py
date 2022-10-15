import sys
sys.stdin = open('소수의곱_input.txt')
import heapq

k, n = map(int,input().split())
arr = list(map(int,input().split()))
q = []


for num in arr :
    heapq.heappush(q,num)

for i in range(n) :
    num = heapq.heappop(q)
    for j in range(k) :
        new = num * arr[j]
        heapq.heappush(q, new)

        if num % arr[j] == 0 :
            break
print(num)