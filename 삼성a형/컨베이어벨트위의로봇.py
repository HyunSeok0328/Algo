import sys
sys.stdin = open('컨베이어벨트위의로봇_input.txt')

n, k = map(int,input().split())
matrix = list(map(int,input().split()))
robot = [0] * (2 * n)
def rotate(arr) :
    global n
    global robot
    newarr = [0] * (2* n)

    for i in range(len(arr)-1,-1,-1) :
        newarr[i] = arr[i-1]
        robot[i] = robot[i-1]
        robot[n-1] = 0

    for i in range(n-2,-1,-1) :
        if robot[i] == 1 and robot[i + 1] == 0 and newarr[i + 1] >= 1:
            robot[i + 1] = 1
            robot[i] = 0
            newarr[i + 1] -= 1
        robot[n-1] = 0

    if newarr[0] != 0 and robot[0] == 0:
        robot[0] = 1
        newarr[0] -= 1


    return newarr
cnt = 0
ans = 0
while True :
    matrix = rotate(matrix)
    cnt += 1
    if matrix.count(0) >= k :
        break
print(cnt)

