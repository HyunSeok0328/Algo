import sys
sys.stdin = open('체인_input.txt')
from collections import deque

N = int(input())
chain = deque(sorted(list(map(int,input().split()))))
ans = 0
while True:
    chain[0] -= 1
    ans += 1
    x = chain.pop()
    y = chain.pop()
    chain.append(x+y)
    if chain[0] == 0:
        chain.popleft()
    if len(chain) == 1:
        break
print(ans)