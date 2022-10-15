import sys
sys.stdin = open('최소힙_input.txt')
from sys import stdin
import heapq
n = int(stdin.readline())
q = []
for i in range(n) :
    x = int(stdin.readline())
    if x == 0 :
        if not q :
            print(0)
        else :
            print(heapq.heappop(q))
    else :
        heapq.heappush(q, (x))
