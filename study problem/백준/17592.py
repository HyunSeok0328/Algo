import sys
# sys.stdin = open('17592_input.txt')
input = sys.stdin.readline
N = int(input())
x = 0
result = 0
arr = []

for i in range(N) :
    arr.append(list(map(int, input().split())))
    if arr[0][0] == 0 :
        arr.pop(0)
    else :
        if arr[-1][0] == 0 :
            arr.pop()
            arr[-1][2] -= 1
            if arr[-1][2] == 0:
                result += arr[-1][1]
                x -= arr[-1][2]
                arr.pop()
        elif arr[-1][2] == 0 :
            result += arr[-1][1]
            x -= arr[-1][2]
            arr.pop()
        else :
            arr[-1][2] -= 1
            if arr[-1][2] == 0:
                result += arr[-1][1]
                x -= arr[-1][2]
                arr.pop()

print(result)
# for i in range(N) :
#     if arr[x][2] == 0 :
#         x -= 1
#     if arr[i][0] == 0 :
#         arr[x][2] -= 1
#
#     else :
#         x = i
#         arr[x][2] -= 1
#
#     if arr[x][2] == 0 :
#         result += int(arr[x][1])
# print(result)