a1, b1, c1, d1, e1, f1, g1, h1, i1 ,j1  = map(int, input().split())
a2, b2, c2, d2, e2, f2, g2, h2, i2 ,j2  = map(int, input().split())
list_a = []
list_b = []
list_a.append(a1)
list_a.append(b1)
list_a.append(c1)
list_a.append(d1)
list_a.append(e1)
list_a.append(f1)
list_a.append(g1)
list_a.append(h1)
list_a.append(i1)
list_a.append(j1)
list_b.append(a2)
list_b.append(b2)
list_b.append(c2)
list_b.append(d2)
list_b.append(e2)
list_b.append(f2)
list_b.append(g2)
list_b.append(h2)
list_b.append(i2)
list_b.append(j2)
result1 = 0
result2 = 0
win = "D"
for i in range(10) :
    if list_a[i] == list_b[i] :
        result1 += 1
        result2 += 1
    elif list_a[i] > list_b[i] :
        result1 += 3
        win = "A"
    else :
        result2 +=3
        win = "B"
    
if result1 > result2 :
    print(result1)
    print(result2)
    print("A")
elif result2 > result1 :
    print(result1)
    print(result2)
    print("B")
else :
    print(result1)
    print(result2)
    print(win)

