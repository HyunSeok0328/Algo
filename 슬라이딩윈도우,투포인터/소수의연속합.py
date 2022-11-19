import sys
sys.stdin = open('소수의연속합_input.txt')

n = int(input())
m = int(n**0.5)
a = [0] * (n+1)
prime_list = []
value = 0
cnt = 0
left , right = 0 , 0
for i in range(2,m+1) :
    if a[i] == 0 :
        for j in range(i+i,n+1,i) :
            a[j] = 1
for i in range(2,len(a)) :
    if a[i] == 0 :
        prime_list.append(i)

# for i in range(len(prime_list)) :
#     for j in range(len(prime_list)-i) :
#         value += prime_list[i+j]
#         if value == n :
#             cnt += 1
#         if value > n :
#             value = 0
#             break
# print(cnt)
# for i in range(len(prime_list)) :
#     for j in range(len(prime_list)-i) :
#         value += prime_list[i+j]
#         if value == n :
#             cnt += 1
#         if value > n :
#             value = 0
#             break
while True :
    if value == n :
        cnt += 1
        value -= prime_list[left]
        left += 1
    elif value > n :
        value -= prime_list[left]
        left += 1
    elif right == len(prime_list) :
        break
    else :
        value += prime_list[right]
        right += 1
# while True :
#     if value == n :
#         cnt += 1
#         value -= prime_list[left]
#         left += 1
#     elif value > n :
#         value -= prime_list[left]
#         left += 1
#     elif right == len(prime_list) :
#         break
#     else :
#         value += prime_list[right]
#         right += 1


print(cnt)