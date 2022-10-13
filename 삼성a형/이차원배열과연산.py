import sys
sys.stdin = open('이차원배열과연산_input.txt')

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

def calculate(arr, dir):

    new_arr = []
    length = 0
    for row in arr :
        num_cnt = []
        new_row = []
        for num in set(row) :
            if num == 0 :
                continue
            cnt = row.count(num)
            num_cnt.append((num,cnt))
        num_cnt = sorted(num_cnt, key=lambda x:[x[1],x[0]])
        for num,cnt in num_cnt :
            new_row += (num,cnt)
        new_arr.append(new_row)
        length = max(length, len(new_row))

    for row in new_arr :
        row += [0] * (length - len(row))
        if len(row) > 100 :
            row = row[:100]
    if dir == 'C' :
        return list(zip(*new_arr))
    else :
        return new_arr
time = 0
while True:
    if time > 100:
        time = -1
        break
    if 0 <= r-1 < len(arr) and 0 <= c-1 < len(arr[0]) and arr[r-1][c-1] == k:
        break
    if len(arr) >= len(arr[0]):
        arr = calculate(arr, 'R')
    else:
        arr = calculate(list(zip(*arr)), 'C')
    time += 1
print(time)


