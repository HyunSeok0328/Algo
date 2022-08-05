import sys
sys.stdin = open('센서_input.txt')

N = int(input())
K = int(input())
arr = list(map(int,input().split()))
tmp = []
arr.sort()
if K >= N :
    print(0)
else :
    for i in range(1,len(arr)) :
        tmp.append(arr[i] - arr[i-1])
    tmp.sort(reverse=True)
    for _ in range(K-1) :
        tmp.pop(0)
    print(sum(tmp))