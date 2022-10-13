import sys
sys.stdin = open('스타트와링크_input.txt')
from itertools import permutations,combinations

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
member = list(range(n))
ans = float('inf')
for start in list(combinations(member,n//2)) :
    start_total = link_total = 0
    link = list(set(member) - set(start))
    for i,j in list(combinations(start,2)) :
        start_total += arr[i][j]
        start_total += arr[j][i]
    for i, j in list(combinations(link,2)) :
        link_total += arr[i][j]
        link_total += arr[j][i]
    ans = min(ans, abs(start_total-link_total))
print(ans)

