import sys
sys.stdin = open('수들의합2_input.txt')

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.append(0)
cnt = 0
value = 0
for i in range(n) :
    for j in range(n-i) :
        value += arr[i+j]
        if value == m :
            cnt += 1
            value = 0
            break
        elif value > m :
            value = 0
            break
    value = 0

print(cnt)