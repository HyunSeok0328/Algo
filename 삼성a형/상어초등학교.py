import sys
sys.stdin = open('상어초등학교_input.txt')

n = int(input())
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n*n) :
    arr.append(list(map(int,input().split())))

cls = [[0] * n for _ in range(n)]

for order in range(n*n) :
    student = arr[order]
    tmp = []
    for x in range(n) :
        for y in range(n) :
            if cls[x][y] == 0 :
                like = 0
                space = 0
                for k in range(4) :
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n :
                        if cls[nx][ny] in student[1:] :
                            like += 1
                        if cls[nx][ny] == 0 :
                            space += 1
                tmp.append((like,space,x,y))
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    cls[tmp[0][2]][tmp[0][3]] = student[0]
result = 0




for i in range(n) :
    for j in range(n) :
        cnt = 0
        for order in range(n*n) :
            student = arr[order]
            if cls[i][j] == arr[order][0] :
                for k in range(4) :
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<= nx < n and 0<= ny < n :
                        if cls[nx][ny] in arr[order][1:] :
                            cnt += 1
        if cnt == 0 :
            result += 0
        elif cnt == 1 :
            result += 1
        elif cnt == 2 :
            result += 10
        elif cnt == 3 :
            result += 100
        elif cnt == 4 :
            result += 1000
print(result)