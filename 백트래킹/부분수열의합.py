import sys
sys.stdin = open('부분수열의합_input.txt')

cnt , tmp = 0, 0
def dfs(index):
    global tmp, cnt
    if index == N:
        return

    if tmp + arr[index] == S:
        cnt += 1

    dfs(index + 1)
    tmp += arr[index]
    dfs(index + 1)
    tmp -= arr[index]
N, S = map(int,input().split())
arr = list(map(int,input().split()))
dfs(0)
print(cnt)