import sys
sys.stdin = open('수묶기_input.txt')

n = int(input())
pos = []
neg = []
ans = 0
for i in range(n) :
    x = int(input())
    if x > 1 :
        pos.append(x)
    elif x == 1 :
        ans += 1
    else :
        neg.append(x)
pos.sort(reverse=True)
neg.sort()

if len(pos) % 2 == 0 :
    for i in range(0,len(pos), 2) :
        ans += pos[i] * pos[i+1]
else :
    for i in range(0, len(pos)-1, 2):
        ans += pos[i] * pos[i+1]
    ans += pos[-1]

if len(neg) % 2 == 0 :
    for i in range(0,len(neg), 2) :
        ans += neg[i] * neg[i+1]
else :
    for i in range(0,len(neg)-1, 2) :
        ans += neg[i] * neg[i + 1]
    ans += neg[-1]
print(ans)