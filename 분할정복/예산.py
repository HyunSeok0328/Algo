import sys
sys.stdin = open('예산_input.txt')

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
start = 1
end = max(arr)

while start <= end :
    mid = (start + end) // 2
    tmp = 0
    for money in arr :
        if money > mid :
            tmp += mid
        else :
            tmp += money
    if tmp <= m :
        start = mid +1
    else :
        end = mid - 1
print(end)