import sys
sys.stdin = open('악마게임_input.txt')

m = input()
N = int(input())
j = 0
dap = {}
flag = 0
def word() :
    ans = int(g) / (len(w) - len(m))
    dap[w] = ans

for i in range(N) :
    w, g = input().split()
    for i in w :
        if i == m[j] :
            j += 1
            if j == len(m)  :
                word()
                j = 0
                break
    j = 0

if dap :
    sort_arr = (sorted(dap.items(), key = lambda item: item[1], reverse=True))

    print(sort_arr[0][0])
else :
    print('No Jam')






