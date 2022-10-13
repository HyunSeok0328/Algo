import sys
sys.stdin = open('과제_input.txt')

N = int(input())
homeworks = []
visit = [0] * 1001

homeworks = [list(map(int,input().split())) for _ in range(N)]
homeworks.sort(key=lambda x: x[1], reverse=True)
answer = 0
for day, worth in homeworks:
    # 과제를 할 날짜 탐색
    while day > 0 and visit[day]:
        day -= 1
    # 과제를 할 날짜가 없으면 패스
    if day == 0:
        continue
    else:
        visit[day] = True
        answer += worth

print(answer)