import sys
sys.stdin = open('보글게임_input.txt')

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def dfs(x,y,cnt) :
    global word_len,flag
    if cnt > word_len :
        return
    elif cnt == word_len :
        flag = 1
        return
    for i in range(8) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 :
            if word_list[cnt] == arr[nx][ny] :

                dfs(nx,ny,cnt+1)



c = int(input())
for tc in range(1,c+1) :
    # visit = [[0] * 5 for _ in range(5)]
    arr = [list(map(str,input())) for _ in range(5) ]
    n = int(input())
    for _ in range(n) :
        word_list = list(map(str,input()))
        word_len = len(word_list)
        flag = 0
        for i in range(5) :
            for j in range(5) :
                if arr[i][j] == word_list[0] :
                    dfs(i,j,1)
        if flag == 1 :
            print(f'{"".join(word_list)} YES')

        else :
            print(f'{"".join(word_list)} NO')