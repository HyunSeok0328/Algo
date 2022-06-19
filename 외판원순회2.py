import sys
sys.stdin = open('외판원순회2_input.txt')
import sys
N = int(sys.stdin.readline())
from itertools import permutations
arr = [list(map(int,input().split())) for _ in range(N)]
min_cost = float('inf')


for route in permutations(range(N)) :
    ans = 0
    route = route + (route[0],)
    flag = 0
    for j in range(len(route)-1) :
        x, y = route[j], route[j+1]
        cost = arr[x][y]
        ans += cost
        if cost <= 0 or ans >= min_cost :
            flag = 1
            break
    if flag == 0 :
        min_cost = min(ans,min_cost)
print(min_cost)



