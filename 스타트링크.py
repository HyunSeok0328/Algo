import sys
sys.stdin = open('스타트링크_input.txt')

from collections import deque

f,s,g,u,d = map(int,input().split())
visit = [0] * (f+1)
q = deque()
q.append(s)
visit[s] = 1
def bfs() :


    while q :
        x = q.popleft()

        if x == g :
            print(visit[x] - 1)
            return
        for nx in (x-d , x+u) :
            if 1 <= nx < f+1 and visit[nx] == 0 :
                visit[nx] = visit[x] + 1
                q.append(nx)
    print('use the stairs')
bfs()