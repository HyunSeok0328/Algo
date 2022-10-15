import sys
sys.stdin = open('연습_input.txt')
s = str(input())
arr = list(s)
answer = 0
cnt = 0
for i in range(len(arr)) :
    for j in range(1,(len(arr)//2)+1) :
        if (i-j) >= 0 and (i+j)< len(arr) :
            if arr[i-j] == arr[i+j] :
                cnt += 1
            else :
                break
    answer = max(answer,cnt)
    cnt = 0
answer = (answer * 2) + 1
print(answer)