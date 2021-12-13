import sys
sys.stdin = open("1388_input.txt")

N,M = map(int,input().split())

arr = [list(input()) for _ in range(M)]
cnt = 0
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == '-' :
            cnt += 1
            while j < M-1 :
                j+=1
                if arr[i][j] == '-' :
                    break
                elif arr[i][j] == '|' :
                    break
            break
        if arr[i][j] == '|' :
            cnt += 1
            while j < M-1 :
                j+=1
                if arr[i][j] == '-' :
                    break
                elif arr[i][j] == '|' :
                    break
            break


print(cnt)
