import sys
sys.stdin = open('숨바꼭질3_input.txt')

from collections import deque
q = deque()
ans = 987654321
visit = [-1] * 1000001
N,K = map(int,input().split())
visit[N] = 0
q.append(N)


while q :
    x = q.popleft()
    if x == K:
        print(visit[x])
        break
    for nx in (2*x, x+1, x-1) :
        if 0 <= nx < 1000001 and visit[nx] == -1 :
            if nx == x*2 :
                visit[nx] = visit[x]
                q.appendleft(nx)
            else :
                visit[nx] = visit[x] + 1
                q.append(nx)



