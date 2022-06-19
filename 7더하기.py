import sys
sys.stdin = open('7더하기_input.txt')

flag = 0
text = ''



tmp = 0
code = ['063','010','093','079','106','103','119','011','127','107']
while text != 'BYE' :
    text = input()
    ans = 0
    aans = ''
    bans = ''
    a = ''
    b = ''
    if text == 'BYE' :
        break
    for i in text :
        if i == '+' :
            flag = 1
            continue
        elif i == '=' :
            ans = int(aans) + int(bans)
            continue
        if flag == 0  :
            a += i
            tmp += 1
        elif flag == 1 :
            b += i
            tmp += 1
        if tmp == 3 :
            for j in range(len(code)) :
                if a == code[j] :
                    aans += str(j)
                elif b == code[j] :
                    bans += str(j)
            tmp = 0
            a = ''
            b = ''
    flag = 0
    real = ''
    dap = str(ans)
    for _ in range(len(dap)) :
        real += code[int(dap[_])]
    print(text+real)


