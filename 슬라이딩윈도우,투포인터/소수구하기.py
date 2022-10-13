import sys
sys.stdin = open('소수구하기_input.txt')

m,n = map(int,input().split())

arr = [0] * (n+1)
k = int(n**0.5)
for i in range(2,k+1) :
    if arr[i] == 0 :
        for j in range(i+i,n+1,i) :
            arr[j] = 1
for k in range(m,len(arr)) :
    if arr[k] == 0 :
        print(k)