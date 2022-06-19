import sys
sys.stdin = open('바이러스_input.txt')

N = int(input())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)
cnt = 0
for i in range(M) :
    a,b = map(int,input().split())
    arr[a][b] = arr[b][a] = 1

def dfs(V) :
    visit[V] = 1
    global cnt
    for i in range(1,N+1) :
        if visit[i] == 0 and arr[V][i] == 1 :
            dfs(i)
            cnt+=1



dfs(1)
print(cnt)