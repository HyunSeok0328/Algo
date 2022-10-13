import sys
sys.stdin = open('색종이붙이기_input.txt')

def func(x,y,cnt) :
    global ans
    if y >= 10 :
        ans = min(ans,cnt)
        return
    if x >= 10 :
        func(0,y+1,cnt)
        return

    if arr[x][y] == 1 :
        for k in range(5) :
            if paper[k] == 5 :
                continue
            if x + k >= 10 or y + k >= 10 :
                continue

            flag = 0
            for i in range(x, x+k+1) :
                for j in range(y, y+k+1) :
                    if arr[i][j] == 0 :
                        flag = 1
                        break
                if flag == 1 :
                    break
            if flag == 0 :
                for i in range(x, x+k+1) :
                    for j in range(y, y+k+1) :
                        arr[i][j] = 0
                paper[k] += 1
                func(x+k+1,y,cnt+1)
                paper[k] -= 1
                for i in range(x, x+k+1) :
                    for j in range(y, y+k+1) :
                        arr[i][j] = 1
    else :
        func(x+1,y,cnt)


arr = [list(map(int,input().split())) for _ in range(10)]
paper = [0] * 5
ans = 26
func(0,0,0)
if ans >= 26 :
    print(-1)
else :
    print(ans)