import sys
sys.stdin = open('0만들기_input.txt')

def solve(tmp, ans) :
    global N
    if tmp == N :
        tmp2 = ans.replace(' ','')
        if eval(tmp2) == 0:
            print(ans)
        return

    solve(tmp + 1 , ans + ' ' + str(tmp+1))
    solve(tmp + 1 , ans + '+' + str(tmp+1))
    solve(tmp + 1, ans + '-' + str(tmp+1))


T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    solve(1 , '1')
    print('')




