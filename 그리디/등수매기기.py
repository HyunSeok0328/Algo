import sys
sys.stdin = open('등수매기기_input.txt')

N = int(input())

arr = []
arr2 = []
total = 0
for i in range(1,N+1) :
    arr.append(int(input()))
    arr2.append(i)
arr.sort()
for j in range(N) :
    total += abs(arr[j] - arr2[j])
print(total)
