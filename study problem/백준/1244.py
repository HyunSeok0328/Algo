import sys
sys.stdin = open('1244_input.txt')

N = int(input())
arr = list(map(int,input().split()))
student = int(input())
cnt = 1
for i in range(student) :
    gender , number = map(int,input().split())
    ans_number = number
    if gender == 1 :
        while ans_number <= N :
            cnt +=1
            if arr[ans_number-1] == 1:
                arr[ans_number-1] = 0
            else :
                arr[ans_number-1] = 1
            ans_number= number*cnt
    else :
        cnt =1
        if arr[number-1] == 1 :
            arr[number-1] = 0
        else :
            arr[number-1] = 1
        if number - 1 + cnt >= N:
            break
        while arr[number-1-cnt] == arr[number-1+cnt] :
            if number-1-cnt < 0 :
                break
            if arr[number-1-cnt] == arr[number-1+cnt] :
                if arr[number-1-cnt] == 1 :
                    arr[number - 1 - cnt] = 0
                else :
                    arr[number - 1 - cnt] = 1
                if arr[number-1+cnt] == 1 :
                    arr[number - 1 + cnt] = 0
                else:
                    arr[number - 1 + cnt] = 1
            else :
                if arr[number-1] == 1:
                    arr[number-1] = 0
                else :
                    arr[number-1] = 1
            cnt += 1
            if number-1+cnt >= N :
                break
cnt = 0
for i in arr :
    cnt += 1
    print(i,end=' ')
    if cnt >= 20 :
        cnt = 0
        print()



