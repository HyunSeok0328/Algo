import sys
sys.stdin = open('초콜릿식사_input.txt')

k = int(input())

choco = 1
while k > choco:
    choco *= 2

print(choco, end=" ")

n = 0
while True:
    if k % choco == 0:
        print(n)
        break
    else:
        choco //= 2
        n += 1