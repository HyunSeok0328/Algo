import sys
sys.stdin = open('치킨배달_input.txt')

def find(n, k) :
    global ans
    if n == M :
        ans = min(ans,dis())
        return
    for i in range(k, len(chicken)) :
        choice.append(chicken[i])
        find(n+1,i+1)
        choice.pop()

def dis() :
    global ans
    sum = 0
    for x,y in home :
        cnt = N*N
        for cx,cy in choice :
            chk = abs(x-cx) + abs(y-cy)
            cnt = min(cnt,chk)
        sum += cnt
        if sum > ans :
            return ans
    return sum

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))
choice = []
ans = 987654321
find(0,0)
print(ans)