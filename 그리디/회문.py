import sys
sys.stdin = open('회문_input.txt')

# T = int(sys.stdin.readline())
# flag = 0
# for i in range(T) :
#     arr = list(input())
#     while arr :
#         if len(arr) == 1 :
#             break
#         if arr[0] == arr[-1] :
#             arr.pop(0)
#             arr.pop(-1)
#         elif arr[0] != arr[-1] and flag == 0 :
#             if arr[1] == arr[-1] :
#                 arr.pop(0)
#             elif arr[0] == arr[-2] :
#                 arr.pop(-1)
#             else :
#                 arr.pop(0)
#
#             flag = 1
#         elif arr[0] != arr[-1] and flag == 1 :
#             flag = 2
#             break
#
#     if flag == 0 :
#         print(0)
#     elif flag == 1 :
#         print(1)
#     elif flag == 2 :
#         print(2)
#     flag = 0

def check(left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
def twopointer(left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if check(left+1, right) or check(left, right-1):
                return 1
            return 2
    return 0
T = int(input())
for _ in range(T):
    s = input()
    print(twopointer(0, len(s)-1))