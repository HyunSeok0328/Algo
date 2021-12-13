N, m, M, T,R  = map(int , input().split())

cnt = 0
cnt2 = 0
result = 0
cnt3 =0
value = m
while cnt3 != N :
    cnt+=1
    value = value+T
    result += 1
    cnt3+=1
    if m+T > M :
        result = -1
    
    if value >= M-T :
        while value > M-T and cnt3 != N and R != 0 and value > 0:
            value = value - R
            result += 1
            cnt = 0
            
    if R == 0 :
        result = -1
    if value < m :
            value = m
print(result)