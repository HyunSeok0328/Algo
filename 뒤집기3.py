import sys
sys.stdin = open('뒤집기3_input.txt')

ans = ''
text = input()
for i in len(text) :
    ans += text[i]