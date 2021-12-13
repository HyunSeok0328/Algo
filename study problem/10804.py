test_case = 'bdppq'
test_list = []
for i in range(len(test_case)) :
    test_list.append(test_case[-(i+1)])
    if test_list[i] == 'p' :
        test_list[i] = test_list[i].replace('p','q')
    elif test_list[i] == 'q' :
        test_list[i] = test_list[i].replace('q','p')
    elif test_list[i] == 'b' :
        test_list[i] = test_list[i].replace('b','d')
    elif test_list[i] == 'd' :
        test_list[i] = test_list[i].replace('d','b') 
for x in test_list :
    print(x,end='')

