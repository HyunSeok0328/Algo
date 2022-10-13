import sys
sys.stdin = open('소수사이수열_input.txt')

T = int(input())
n = 1299709
prime_list = []
l = int(n**0.5)
arr = [0] * (n+1)
ans = 0
for i in range(2,l+1) :
    if arr[i] == 0 :
        for j in range(i+i,n+1,i) :
            arr[j] = 1
for i in range(2,n+1) :
    if arr[i] == 0 :
        prime_list.append(i)
for tc in range(1,T+1) :
    k = int(input())
    for i in range(len(prime_list)+1) :
        if prime_list[i] < k < prime_list[i+1] :
            ans = prime_list[i+1] - prime_list[i]
            break
        elif prime_list[i] == k :
            ans = 0
            break
    print(ans)
