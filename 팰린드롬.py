import sys
sys.stdin = open('팰린드롬_input.txt')

# n = int(input())
# arr = list(map(int,input().split()))
# m = int(input())
#
# for tc in range(m) :
#     newarr = []
#     flag = 0
#     s, e= map(int,input().split())
#     for i in range(s-1,e) :
#
#         newarr.append(arr[i])
#     for j in range(len(newarr)) :
#         if len(newarr) % 2 == 0 :
#             flag = 1
#             break
#         else :
#             for k in range(len(newarr)//2) :
#                 if (j-k) >= 0 and (j+k) < len(newarr) :
#                     if newarr[j-k] == newarr[j+k] :
#                         continue
#     if flag == 1 :
#         print(0)
#     else :
#         print(1)
n = int(input())
numbers = list(map(int, input().split()))
m = int(input())


dp = [[0] * n for _ in range(n)]

for num_len in range(n):
    for start in range(n - num_len):
        end = start + num_len

        # 시작점과 끝점이 같다면 글자수가 1개이므로 무조건 팰린드롬
        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면
        elif numbers[start] == numbers[end]:
            # 두 글자짜리 문자열이라면 무조건 팰린드롬
            if start + 1 == end:
                dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

# 정답출력하기
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])