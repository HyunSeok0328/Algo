import sys
sys.stdin = open('퇴사_input.txt')

n = int(input())
d = [0] * 20
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    x = arr[i][0] - 1
    d[i] = max(d[i - 1], d[i])
    d[i + x] = max(d[i - 1] + arr[i][1], d[i + x])

print(d[n-1])

