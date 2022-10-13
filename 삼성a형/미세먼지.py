import sys
sys.stdin = open('미세먼지_input.txt')

from collections import deque
r,c,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]


q = deque()

def up_air() :
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny
def down_air() :
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    direct = 0
    before = 0
    x, y = down, 1
    while True :
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0 :
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c :
            direct += 1
            continue
        arr[x][y] , before = before , arr[x][y]
        x = nx
        y = ny
def spread() :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]



ans = 0

for i in range(r) :
    if arr[i][0] == -1 :
        up = i
        down = i +1
        break
for i in range(t) :
    spread()
    up_air()
    down_air()
for i in range(r) :
    for j in range(c) :
        if arr[i][j] > 0 :
            ans += arr[i][j]
print(ans)