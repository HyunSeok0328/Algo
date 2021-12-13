import sys
sys.stdin = open('숨바꼭질_input.txt')

from collections import deque
N, K = map(int,input().split())
q = deque()
ans = 987654321
visit = [0] * 1000001
q.append(N)
def bfs() :
    while q :
        x = q.popleft()
        if x == K :
            print(visit[x])
            break
        for nx in (x-1, x+1, x*2) :
            if 0 <= nx <= 1000000 and visit[nx] == 0:
                visit[nx] = visit[x] + 1
                q.append(nx)

bfs()











