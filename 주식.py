import sys
sys.stdin = open('주식_input.txt')

T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    arr = list(map(int,input().split()))
    answer = 0
    mx = arr[-1]
    for i in range(N - 2, -1, -1):
        if arr[i] > mx:  # 오늘 가격이 mx라면
            mx = arr[i]
        else:
            answer += mx - arr[i]  # 오늘 가격이 최대가 아니라면 최대-지금가격만큼 더한다
    print(answer)
