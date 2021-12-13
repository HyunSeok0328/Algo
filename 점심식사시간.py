import sys
sys.stdin = open('점심식사시간_input.txt')

T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    people = []
    stair = []
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 1 :
                people.append((i,j))
            elif 2<= arr[i][j] <= 10 :
                stair.append((i,j))
        