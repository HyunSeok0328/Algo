import sys
sys.stdin = open('선긋기_input.txt')

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort()
answer = 0
left = right = 0

for start,end in line :
    if answer == 0 :
        answer = abs(end-start)
        left = start
        right = end
        continue
    if left <= start and right >= end :
        continue
    answer += abs(end-start)
    if right > start :
        answer -= abs(right-start)
    left = start
    right = end
print(answer)
