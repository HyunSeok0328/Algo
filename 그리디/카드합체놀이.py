import sys
sys.stdin = open('카드합체놀이_input.txt')

n, m = map(int,input().split())
arr = []
arr = list(map(int,input().split()))
ans = 0
for i in range(m) :
    arr.sort(reverse=True)
    ans = arr[-1] + arr[-2]
    arr[-1] = ans
    arr[-2] = ans
print(sum(arr))