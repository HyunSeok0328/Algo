import sys
import copy
sys.stdin = open('5212_input.txt')

R, C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
newarr = copy.deepcopy(arr)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
stack = 0
startrow = 9999999999
endrow = 0
startcolumn = 999999999999
endcolumn = 0
for i in range(R) :
    for j in range(C) :
        if arr[i][j] == 'X' :
            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    stack += 1
                    continue
                elif arr[nx][ny] =='.' :
                    stack += 1

            if stack >= 3 :
                newarr[i][j] = '.'
                stack = 0
            if k == 3:
                stack = 0

for i in range(R) :
    if 'X' in newarr[i] :
        if startcolumn > i :
            startcolumn = i
        if endcolumn < i :
            endcolumn = i
        for j in range(C) :
            if newarr[i][j] == 'X' :
                if j > startrow :
                    pass
                else :
                    startrow = j
                break
        for j in range(C-1,0,-1) :
            if newarr[i][j] == 'X' :
                if j < endrow :
                    pass
                else :
                    endrow = j
                break
for i in range(startcolumn,endcolumn+1) :
    for j in range(startrow,endrow+1) :
        print(newarr[i][j], end='')
    print()