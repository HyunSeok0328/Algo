x_list= []
y_list= []
for i in range(3):
        x, y = map(int , input().split())
        x_list.append(x)
        y_list.append(y)

for i in range(3) :
    if x_list[i]==x_list[i-1] :
        print(x_list[i-2])
for j in range(3) :
    if  y_list[j]!= y_list[j-1] :
        print( y_list[j-2])