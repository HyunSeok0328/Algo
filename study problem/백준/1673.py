n, k = map(int, input().split())

res = n
while n//k != 0:
    res += n//k
    n = n//k + n%k
print(res)