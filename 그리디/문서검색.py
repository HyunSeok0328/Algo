import sys
sys.stdin = open('문서검색_input.txt')

first = input()
second = input()
cnt = 0
while True :
    idx = first.find(second)
    if idx == -1 :
        break
    cnt += 1
    first = first[idx + len(second):]
print(cnt)
