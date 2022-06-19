import sys
sys.stdin = open('회의실배정_input.txt')

N = int(input())
arr = []

for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])
arr2 = sorted(arr, key=lambda x: (x[1],x[0]))
last = 0
cnt = 0

for i, j in arr2:
  if i >= last:
    cnt += 1
    last = j

print(cnt)
