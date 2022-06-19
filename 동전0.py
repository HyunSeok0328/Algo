import sys
sys.stdin = open('동전0_input.txt')

N, K = map(int,input().split())
arr = []
for i in range(N) :
    arr.append(int(input()))
cnt = 0
while K != 0 :
    for i in range(len(arr)-1,-1,-1) :
        if K >= arr[i] :
            K -= arr[i]
            cnt +=1
            break
print(cnt)
