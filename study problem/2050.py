def change(word) : 
    for i in range(len(word)) :
        print(int(ord(word[i])-64))

change('ABCD')