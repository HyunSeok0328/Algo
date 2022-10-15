import sys
sys.stdin = open('주사위굴리기_input.txt')

n,m ,x, y,k = map(int,input().split())
arr = []
for i in range(n) :
    arr.append(list(map(int,input().split())))
dir_arr = list(map(int,input().split()))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0,0,0,0,0,0]

def turn(dir) :
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if dir == 0 : # 동
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    elif dir == 1 : #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif dir == 2 : #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b
    else :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e

for i in range(k) :
    d = dir_arr[i] -1
    x = x + dx[d]
    y = y + dy[d]
    if 0 <= x < n and 0 <= y < m :
        turn(d)
        if arr[x][y] == 0 :
            arr[x][y] = dice[5]
        else :
            dice[5] = arr[x][y]
            arr[x][y] = 0
        print(dice[0])
    else :
        x = x - dx[d]
        y = y - dy[d]
