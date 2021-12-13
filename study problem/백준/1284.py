import sys
cnt = 0
while cnt !=1 :
    cnt =1
    if x >= 1000 :
        a = x % 10 
        b = x // 10 - (x // 100)*10
        c = x // 100 - (x // 1000)*100
        d = x // 1000
        value = 5
        if a == 1 :
            value += 2
        elif a == 0 :
            value += 4
        else :
            value += 3
        if b == 1 :
            value += 2
        elif b == 0 :
            value += 4
        else :
            value += 3
        if c == 1 :
            value += 2
        elif c == 0 :
            value += 4
        else :
            value += 3
        if d == 1 :
            value += 2
        elif d == 0 :
            value += 4
        else :
            value += 3
        print(value)
    elif x >= 100 :
        a = x % 10 
        b = (x // 10) -10
        c = x // 100
        value = 4
        if a == 1 :
            value += 2
        elif a == 0 :
            value += 4
        else :
            value += 3
        if b == 1 :
            value += 2
        elif b == 0 :
            value += 4
        else :
            value += 3
        if c == 1 :
            value += 2
        elif c == 0 :
            value += 4
        else :
            value += 3
        print(value)
    elif x >= 10 :
        a = x % 10 
        b = x // 10
        value = 3
        if a == 1 :
            value += 2
        elif a == 0 :
            value += 4
        else :
            value += 3
        if b == 1 :
            value += 2
        elif b == 0 :
            value += 4
        else :
            value += 3
        print(value)
    elif x == 0 :
        break
    else :
        a = x % 10
        value = 2
        if a == 1 :
            value += 2
        elif a == 0 :
            value += 4
        else :
            value += 3
        print(value)



