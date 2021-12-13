import sys
sys.stdin = open('17938_input.txt')

N = int(input())

P, T = map(int,input().split())
ans = 0
hand = 0
mode = 0
mode2 = 1
for i in range(T) :

    if mode == 0 :
        hand += 1
        if hand == (2*N) :
            mode = 1
    else :
        hand -= 1
        if hand == 1 :
            mode = 0
    ans = (ans + hand)
    if ans == (2*N) :
        ans = 2*N
    else :
        ans = ans % (2 * N)
for j in range(hand) :
    if ans == P*2 :
        print('Dehet YeonJwaJe ^~^')
        mode2 = 0
        break
    ans -= 1
    if ans == 0:
        ans = N*2

if mode2 == 1 :
    print('Hing...NoJam')

