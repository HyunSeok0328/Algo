import sys
sys.stdin = open('요리사_input.txt')

from itertools import combinations
T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    ans = 9999999999
    arr = [list(map(int,input().split())) for _ in range(N)]

    for graph in combinations(range(1,N+1), N//2) :
        num = list(range(1, N + 1))
        sol1 = 0
        sol2 = 0
        for i in graph :
            num.remove(i)
            for j in graph :
                sol1 += arr[i-1][j-1]
        for x in num :
            for y in num :
                sol2 += arr[x-1][y-1]

        sol = abs(sol1-sol2)
        ans = min(ans,sol)
    print(f'#{tc} {ans}')


