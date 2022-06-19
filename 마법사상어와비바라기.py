import sys
sys.stdin = open('마법사상어와비바라기_input.txt')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
