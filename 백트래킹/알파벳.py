import sys
sys.stdin = open('알파벳_input.txt')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,cnt) :
    global ans
    ans = max(ans, cnt)
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not arr[nx][ny] in alp :
            alp.add(arr[nx][ny])
            dfs(nx,ny,cnt+1)
            alp.remove(arr[nx][ny])



r, c = map(int,input().split())
arr = []
ans = 0
for i in range(r) :
    arr.append(list(map(str,input())))
alp = set()
alp.add(arr[0][0])
dfs(0,0,1)
print(ans)