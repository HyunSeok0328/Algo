import sys
sys.stdin = open('블로그_input.txt')

n, x = map(int,input().split())
arr = list(map(int,input().split()))

if max(arr) == 0 :
    print('SAD')
else :
    value = sum(arr[:x])
    max_value = value
    max_cnt = 1

    for i in range(x,n) :
        value += arr[i]
        value -= arr[i-x]

        if value > max_value :
            max_value = value
            max_cnt = 1

        elif value == max_value :
            max_cnt += 1
    print(max_value)
    print(max_cnt)
