import sys
sys.stdin = open('찾기_input.txt')

def kmp(s, p):
    n = len(s)
    m = len(p)
    table = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    j = 0
    count = 0
    loc = []
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            if j == (m - 1):
                count += 1
                loc.append(i - m + 2)
                j = table[j]
            else:
                j += 1
    print(count)
    print(*loc)

t = input()
p = input()
kmp(t, p)