import sys
sys.stdin = open('암호만들기_input.txt')

def dfs(cnt,idx) :
    if cnt == l :
        co , vo = 0 , 0
        for i in range(l) :
            if ans[i] in cons :
                vo += 1
            else :
                co += 1
        if vo >= 1 and co >= 2 :
            print("".join(ans))
        return
    else :
        for i in range(idx,c) :
            ans.append(arr[i])
            dfs(cnt+1,i + 1)
            ans.pop()




l,c = map(int,input().split())
arr = (list(map(str,input().split())))
arr.sort()
cons = ['a','e','i','o','u']
ans = []
dfs(0,0)
