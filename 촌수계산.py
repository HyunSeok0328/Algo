import sys
sys.stdin = open('촌수계산_input.txt')

from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [ [0] * (n+1) for _ in range(n+1) ]
visited = [0] * (n+1)
answer = -1

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

def bfs(x):
    global answer
    q = deque()
    q.append((x,0))


    while q:
        node, cnt = q.popleft()

        if node == y:
            answer = cnt

        for i in arr[node]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, cnt+1))

bfs(x)

print(answer)