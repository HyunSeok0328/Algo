import sys
sys.stdin = open('게임을만든동준이_input.txt')

n = int(input())
arr = []
ans = 0
for i in range(n) :
    x = int(input())
    arr.append(x)
for i in range(n,1,-1) :
    while arr[i-1] <= arr[i-2] :
        ans += 1
        arr[i-2] -= 1
print(ans)


