import sys
sys.stdin = open('야구_input.txt')

from itertools import permutations

ans = 0
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for order in permutations((range(1, 9)), 8):
    order = list(order[:3]) + [0] + list(order[3:])
    score = 0
    hitter = 0
    for i in range(N) :
        out = 0
        f,s,t = 0,0,0
        while out < 3 :
            result = arr[i][order[hitter]]

            if result == 0 :
                out += 1
            elif result == 1 :
                score += t
                f,s,t = 1,f,s
            elif result == 2 :
                score += (s+t)
                f,s,t = 0,1,f
            elif result == 3 :
                score += (f+s+t)
                f,s,t = 0,0,1
            elif result == 4 :
                score += (f+s+t+1)
                f,s,t = 0,0,0

            hitter = (hitter+1) % 9
    if ans < score :
        ans = score
print(ans)
