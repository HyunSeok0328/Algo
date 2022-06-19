import sys
sys.stdin = open('마법사상어와파이어볼_input.txt')
from collections import deque


q=deque()
N,M,K = map(int,input().split())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(M) :
    r,c,m,s,d = map(int,input().split())
    q.append((r-1,c-1,m,s,d))
arr = [[0] * N for _ in range(N)]
while K :
    K-=1
    while q :
        x,y,m,s,d = q.popleft()
        nx = (x + dx[d]*s + N) % N
        ny = (y + dy[d]*s + N) % N
        if arr[nx][ny] != 0 :
            arr[nx][ny] += m
            
        else :
            arr[nx][ny] = m



