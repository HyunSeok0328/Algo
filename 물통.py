import sys
sys.stdin = open('물통_input.txt')
from collections import deque

def solve(x,y) :
    if visit[x][y] == 0 :
        visit[x][y] = 1
        q.append((x,y))

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y
        if x == 0 :
            ans.append(z)
        # a->b
        water = min(x,b-y)
        solve(x-water, y+water)
        # a->c
        water = min(x,c-z)
        solve(x-water, y)
        # b->a
        water = min(y, a-x)
        solve(x+water, y-water)
        # b->c
        water = min(y,c-z)
        solve(x, y-water)
        # c->a
        water = min(z, a-x)
        solve(x+water, y)
        # c->b
        water = min(z,b-y)
        solve(x, y+ water)

a, b, c = map(int,input().split())
visit = [[0] * 201 for _ in range(201)]
ans = []
q = deque()
q.append((0,0))
visit[0][0] = 1
bfs()
ans.sort()
for i in ans :
    print(i, end=" ")