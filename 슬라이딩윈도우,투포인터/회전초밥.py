import sys
sys.stdin = open('회전초밥_input.txt')

n,d,k,c = map(int,input().split())
arr = []
for i in range(n) :
    x= int(input())
    arr.append(x)
lp,rp = 0, 0
ans = 0

while True :
    rp = lp + k
    case = set()
    if lp == n :
        break
    coupon = True
    for i in range(lp,rp) :
        i %= n
        case.add(arr[i])
        if arr[i] == c :
            coupon = False
    cnt = len(case)
    if coupon :
        cnt += 1
    ans = max(ans,cnt)
    lp += 1
print(ans)