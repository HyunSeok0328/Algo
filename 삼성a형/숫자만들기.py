import sys
sys.stdin = open('숫자만들기_input.txt')




def dfs(arr, op_list, op):
    if sum(op_list) == 0:
        arr2.append(cal(arr,op))


    for i in range(0, 4):
        if op_list[i] != 0:
            op_list[i] -= 1
            op.append(i)
            dfs(arr, op_list, op)
            op.pop()
            op_list[i] += 1


def cal(arr, val):
    sum = arr[0]
    for i in range(0, len(val)):
        if val[i] == 0:
            sum += arr[i + 1]
        elif val[i] == 1:
            sum -= arr[i + 1]
        elif val[i] == 2:
            sum *= arr[i + 1]
        elif val[i] == 3:
            sum = int(sum / arr[i + 1])

    return sum



T = int(input())
for TC in range(1, T + 1):
    max_num = 9999999999999999
    min_num = -9999999999999
    N = int(input())
    op_list = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr2 = []
    dfs(arr, op_list, [])

    max_num = max(arr2)
    min_num = min(arr2)
    print("#%d %d" % (TC, max_num - min_num))