import sys
sys.stdin = open('미생물격리_input.txt')

def check(x,y) :
    if y == 0 or y == N-1 or x == 0 or x == N-1 :
        return
def change(idx) :
    if idx == 1:
        return 2
    elif idx == 2 :
        return 1
    elif idx == 3 :
        return 4
    elif idx == 4 :
        return 3
def move(arr) :
    board = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    for x in range(N) :
        for y in range(N) :
            if arr[x][y][0] != 0 :
                value, idx = arr[x][y][0] , arr[x][y][1]
                nx = x + dx[idx]
                ny = y + dy[idx]
                if check(nx,ny) :
                    value //= 2
                    idx = change(idx)
                if value > 0 :
                    board[nx][ny][0] = value
                    board[nx][ny][1] = idx



T = int(input())
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

for tc in range(1,T+1) :
    N, M, K = map(int,input().split())
    arr = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    for i in range(K) :
        x,y,value,idx = map(int,input().split())
        arr[x][y][0] = value
        arr[x][y][1] = idx
    print(arr)
    for i in range(M) :
        arr = move(arr)


