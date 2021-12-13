import sys
sys.stdin = open('12981_input.txt')

R,G,B = map(int,input().split())
cnt = 0

while R >= 4 or G >= 4 or B >= 4 :

    if R >= 4 :
        R -= 3
        cnt +=1
    if G >= 4 :
        G -= 3
        cnt +=1
    if B >= 4 :
        B -= 3
        cnt +=1
if R == 3 and G == 3 and B == 2:
    while R > 0 or G > 0 or B > 0:
        R -= 1
        G -= 1
        B -= 1
        cnt += 1
elif R == 3 and G == 2 and B == 3:
    while R > 0 or G > 0 or B > 0:
        R -= 1
        G -= 1
        B -= 1
        cnt += 1
elif R == 2 and G == 3 and B == 3:
    while R > 0 or G > 0 or B > 0:
        R -= 1
        G -= 1
        B -= 1
        cnt += 1
else :
    while R >= 3 or G >= 3 or B >= 3:

        if R >= 3:
            R -= 3
            cnt += 1
        if G >= 3:
            G -= 3
            cnt += 1
        if B >= 3:
            B -= 3
            cnt += 1
    while R > 0 or G > 0 or B > 0:
        R -= 1
        G -= 1
        B -= 1
        cnt += 1
print(cnt)