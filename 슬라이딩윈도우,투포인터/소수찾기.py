import sys
sys.stdin = open('소수찾기_input.txt')
n = int(input())
matrix= list(map(int,input().split()))
prime_list = []
ans = len(matrix)
a = 1000
b = int(a**0.5)
arr = [0] * (a+1)
for i in range(2,a+1) :
    if arr[i] == 0 :
        for j in range(i+i,a+1,i) :
            arr[j] = 1
for i in range(2,len(arr)) :
    if arr[i] == 0 :
        prime_list.append(i)
for i in range(len(matrix)) :
    if matrix[i] not in prime_list :
        ans -= 1
print(ans)