import sys
sys.stdin = open('토마토2_input.txt')

from collections import deque

def dfs() :
    while q :
        a, b, c = q.popleft()
        for i in range(6):
            ny = a + dy[i]
            nx = b + dx[i]
            nz = c + dz[i]


q = deque()
M,N,H = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(N)] for __ in range(H)]
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if arr[i][j][k] == 1 :
                q.append((i,j,k))
dfs()