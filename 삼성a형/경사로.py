import sys
sys.stdin = open('경사로_input.txt')

def check(n,l, route) :
    ramp = [0] * n
    for i in range(n-1) :
        if route[i] != route[i+1] :
            if abs(route[i] - route[i+1]) > 1 :
                return False
            else :
                if route[i] - route[i+1] == 1 :
                    if i+1+l > n :
                        return False
                    check = route[i+1]
                    for j in range(i+1,i+1+l) :
                        if ramp[j] or route[j] != check :
                            return False
                        ramp[j] = 1
                elif route[i] - route[i+1] == -1 :
                    if i-l < -1 :
                        return False
                    check = route[i]
                    for j in range(i,i-l,-1) :
                        if ramp[j] or route[j] != check :
                            return False
                        ramp[j] = 1
    return True




n, l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
for r in arr :
    if check(n,l,r) :
        cnt += 1
for c in range(n) :
    if check(n,l,[arr[r][c] for r in range(n)]) :
        cnt += 1
print(cnt)