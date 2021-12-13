import sys
sys.stdin = open('20006_input.txt')

p, m = map(int,input().split())
arr = []
for i in range(p) :
    l, n = input().split()
    arr.append([int(l), n])
rooms = []


for lv, id in arr:
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m:
            continue

        # 들어갈 수 있는 방이 있으면 입장
        if rooms[i][0] - 10 <= lv <= rooms[i][0] + 10:
            flag = True
            rooms[i][1].append([lv, id])
            break

    # 대기방에 들어 갈 수 없으면 새로운 방 생성
    if not flag:
        rooms.append([lv, [[lv, id]]])
