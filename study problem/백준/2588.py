n = int(input())
m = int(input())
res1 = 0
res2 = 0
res3 = 0
res4 = 0

res1 = n * (m%10)
res2 = n *((m//10)%10) 
res3 = n * (m//100) 
res4 = n*m
print(res1)
print(res2)
print(res3)
print(res4)