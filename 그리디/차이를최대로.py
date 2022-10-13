import sys
sys.stdin = open('차이를최대로_input.txt')
from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))

perm = list(permutations(arr,n))
total=0
ans = 0
for i in range(len(perm)) :
    for j in range(n-1) :
        total += abs(perm[i][j]-perm[i][j+1])
    ans = max(ans, total)
    total = 0

print(ans)

