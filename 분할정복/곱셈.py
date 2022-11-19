import sys
sys.stdin = open('곱셈_input.txt')

A,B,C = map(int,input().split())

def solve(a,b) :
    if b == 1 :
        return a % C
    tmp = solve(a,b//2)
    if b % 2 == 0 :
        return (tmp**2) % C
    else :
        return (tmp**2) * a % C

print(solve(A,B))