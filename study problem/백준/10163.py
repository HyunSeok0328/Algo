import sys
sys.stdin = open('10163_input.txt')

N = int(input())

arr = [[0] * 1001 for _ in range(1001)]
cnt = 0
for tc in range(1,N+1) :
    x , y , width, height = map(int,input().split())


    for i in range(width) :
        for j in range(height) :
            if arr[x+i][y+j] != tc :
                arr[x + i][y + j] = tc
for k in range(1,N+1):
    cnt = 0
    for i in range(1001) :
        for j in range(1001) :
            if arr[i][j] == k :
                cnt += 1
    print(cnt)



