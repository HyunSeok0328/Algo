result = 0
cnt=0
n, t = map(int , input().split())
for i in range(t) :
    if result >= 2*n :
        while result != 1 :
            if  cnt == t :
                break
            else : 
                result -=1
                cnt+=1     
    elif cnt == t :
        break
    else : 
        result+=1
        cnt+=1
print(result)