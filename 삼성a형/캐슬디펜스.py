import sys
sys.stdin = open('캐슬디펜스_input.txt')
from itertools import combinations
from collections import deque
import copy
n, m, d = list(map(int, input().split()))
arr = [[0] * m for _ in range(n + 1)]

ENEMY = 1
NONE = 0
answer = 0

turn = m + 1

positions = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = data[j]
        positions.append((i, j))
        if arr[i][j] == 1:
            turn = min(turn, i)
# 최대 시행 횟수
turn = n - turn

columns = [i for i in range(m)]
comb = list(combinations(columns, 3))


# 스택을 이용해 아래로 1칸씩 적을 이동시킨다.
def move_enemy(origin: list[list[int]]):
    line_stack = dict()
    for k in range(m):
        line_stack[k] = deque()
        line_stack[k].append(0)

    # 맨 아랫줄은 제외하고 스택에 넣는다.
    for a in range(n - 1):
        for b in range(m):
            line_stack[b].append(origin[a][b])

    for a in range(n):
        for b in range(m):
            origin[n - a - 1][b] = line_stack[b].pop()


def find_nearest(archer_y: int, origin: list[list[int]]):
    pos_set = set()
    for a in range(n + 1):
        for b in range(m):
            difference = abs(n - a) + abs(archer_y - b)
            if difference <= d and origin[a][b] == ENEMY:
                pos_set.add((difference, a, b))

    pos_list = list(sorted(pos_set, key=lambda o: (o[0], o[2])))
    if pos_list:
        return pos_list[0][1], pos_list[0][2]
    else:
        return None


def find_enemy(result, origin: list[list[int]]) -> list:
    target = set()

    for y in result:
        nearest = find_nearest(y, origin)
        if nearest is not None:
            target.add((nearest[0], nearest[1]))
    return list(target)


for rst in comb:
    score = 0
    temp = copy.deepcopy(arr)
    for count in range(turn):
        target_list = find_enemy(rst, temp)

        for p, q in target_list:
            temp[p][q] = NONE

        score += len(target_list)

        move_enemy(temp)

    answer = max(answer, score)

print(answer)

