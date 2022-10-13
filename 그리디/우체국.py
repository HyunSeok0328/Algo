import sys
sys.stdin = open('우체국_input.txt')

# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# sum = float('inf')
# ans = 0
# for i in range(N) :
#     hap = 0
#     for j in range(N) :
#         hap += abs(i-j) * arr[j][1]
#     if sum > hap :
#         sum = min(hap,sum)
#         ans = i
# print(ans+1)


all_people = 0

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N) :
    all_people += arr[i][1]

arr.sort(key= lambda x: x[0])

count = 0
for i in range(N):
    count += arr[i] [1]
    if count >= all_people/2:
        print (arr[i][0])
        break