import sys
input = sys.stdin.readline
k, a, b = map(int,input().split())
cnt = 0
i=1
number = k
if a < 0 and b < 0 :
    number = -k
    while number >= a:
        if a <= number <= b:
            i += 1
            number = -(k * i)
            cnt += 1
        else:
            i += 1
            number = -(k * i)
elif a < 0 and b > 0 :
    cnt =1
    while number <= b :
        if a < 0 and b > 0 and number >= 0:
            i += 1
            number = k * i
            cnt += 1
        else :
            i += 1
            number = k * i
    number =-k
    i =1
    while number >= a :
        if a <= number <= 0 :
            i += 1
            number = -(k * i)
            cnt += 1
        else :
            i += 1
            number = -(k * i)
elif a >0 and b > 0 :
    while number <= b :
        if a > 0 and b > 0 and number >= a:
            i += 1
            number = k*i
            cnt += 1
        else :
            i += 1
            number = k * i
print(cnt)