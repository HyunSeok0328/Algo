import sys
sys.stdin = open('보물상자비밀번호_input.txt')

T = int(input())

for tc in range(1,T+1) :
    N, K = map(int,input().split())
    arr = list(input())
    new_arr = []

    for i in range(int(N/4)) :
        number = arr.pop(-1)
        arr.insert(0,number)
        for j in range(0,N,int(N/4)) :
            str = ''
            for k in range(j,j+int(N/4)) :
                str += arr[k]
            new_arr.append(str)
    set_arr = list(set(new_arr))
    set_arr.sort(reverse=True)
    print(f'#{tc} {int(set_arr[K-1], 16)}')