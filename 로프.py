import sys
sys.stdin = open('로프_input.txt')

N = int(input())
arr = []
value= []
for i in range(N) :
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(N) :
    value.append(arr[i]*(i+1))
print(max(value))
