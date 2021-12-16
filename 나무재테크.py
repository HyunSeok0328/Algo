import sys
sys.stdin = open('나무재테크_input.txt')
from collections import deque
input = sys.stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
tree = deque()
dead = deque()
treetmp = deque()
N,M,K = map(int,input().split())
arr = [[5] * N for _ in range(N)]
arr2 = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M) :
    x,y,z = map(int,input().split())
    tree.append((x-1,y-1,z))

cnt = 0
while K :
    K -= 1
    while tree:
        x, y, z = tree.popleft()
        if arr[x][y] == 0:
            dead.append((x, y, z))
        else:
            arr[x][y] -= z
            if arr[x][y] < 0:
                arr[x][y] += z
                dead.append((x, y, z))
            else:
                treetmp.append((x, y, z + 1))
    while dead :
        x, y, z = dead.popleft()
        arr[x][y] += z//2
    while treetmp :
        x,y,z = treetmp.popleft()
        if z%5 == 0 :
            for i in range(8) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < N and 0 <= ny < N :
                    tree.appendleft((nx,ny,1))
        tree.append((x, y, z))
    for i in range(N):
        for j in range(N):
            arr[i][j] += arr2[i][j]
print(len(tree))


def spring() :
    while tree :
        x,y,z = tree.popleft()
        if arr[x][y] == 0 :
            dead.append((x,y,z))
        else :
            arr[x][y] -= z
            if arr[x][y] < 0 :
                arr[x][y] += z
                dead.append((x,y,z))
            else :
                treetmp.append((x,y,z+1))
def summer() :
    while dead :
        x, y, z = dead.popleft()
        arr[x][y] += z//2
def fall() :
    while treetmp :
        x,y,z = treetmp.popleft()
        tree.append((x, y, z))
        if z%5 == 0 :
            for i in range(8) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < N and 0 <= ny < N :
                    tree.appendleft((nx,ny,1))

def winter() :
    for i in range(N):
        for j in range(N):
            arr[i][j] += arr2[i][j]