import sys
sys.stdin = open('puyopuyo_input.txt')

from collections import deque

def bfs(y, x, color) :
    global check
    q = deque()
    q.append((y,x))
    visit = []
    visit = [(y,x)]
    while q :
        a, b = q.popleft()
        for i in range(4) :
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < 12 and 0 <= nx < 6 and (ny, nx) not in visit:
                if arr[ny][nx] == color:
                    q.append((ny, nx))
                    visit.append((ny, nx))
    if len(visit) >= 4 :
        check = 0
        for i,j in visit :
            arr[i][j] = '.'
arr = [list(map(str,input())) for _ in range(12)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
ans = 0
while True :
    check = 1
    for y in range(12) :
        for x in range(6) :
            if arr[y][x] != '.' :
                bfs(y, x, arr[y][x])
    if check == 1  :
        print(ans)
        break
    ans += 1
    for i in range(6) :
        stack = []
        for j in range(12) :
            if arr[j][i] != '.' :
                stack.append(arr[j][i])
        idx = 11
        while stack :
            arr[idx][i] = stack.pop()
            idx -= 1
        while idx >= 0 :
            arr[idx][i] = '.'
            idx -= 1
