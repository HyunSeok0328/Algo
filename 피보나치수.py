import sys
sys.stdin = open('피보나치수_input.txt')

N = int(input())

def fibo(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

print(fibo(N))