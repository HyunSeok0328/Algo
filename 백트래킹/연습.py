s = "abcabcbb"
s = list(s)
ans = 0
left, right = 0, 1
cnt = 0
while True:
    if s[right] == s[right - 1]:
        cnt = right - left - 1
        ans = max(ans, cnt)
        left = right
        right += 1
    if right >= len(s) - 1:
        cnt = right - left
        ans = max(ans, cnt)
        print(ans)
        break
    elif s[left] != s[right]:
        right += 1
    elif s[left] == s[right]:
        cnt = right - left
        ans = max(ans, cnt)
        left += 1
