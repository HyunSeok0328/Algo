import sys
sys.stdin = open('스티커_input.txt')

T = int(input())
for tc in range(1,T+1) :
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    if n == 1 :
       print(max(arr[0][0],arr[1][0]))
    else :
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

        for i in range(2, n):
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])
        print(max(arr[0][n - 1], arr[1][n - 1]))
