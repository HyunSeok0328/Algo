import sys
sys.stdin = open('치킨배달_input.txt')
from itertools import combinations

N , M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
chicken = []
home = []
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            home.append((i,j))
ans = 987654321
for i in combinations(chicken, M) :
    sum = 0
    for y,x in home :
        cnt = N*N
        for j in i :
            chk = abs(j[0]-x)+abs(j[1]-y)
            cnt = min(cnt,chk)
        sum += cnt
        if sum > ans :
            break
    ans = min(ans,sum)
print(ans)


