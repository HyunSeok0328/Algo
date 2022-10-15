import sys
sys.stdin = open('연습_input.txt')
n = int(input())
arr = [0] * (n+1)
m = int(n**0.5)
for i in range(2,m+1) :
    if arr[i] == 0 :
        for j in range(i+i,n+1,i ):
            arr[j] = 1
for i in range(2,n+1) :
    if arr[i] == 0 :
        print(i)