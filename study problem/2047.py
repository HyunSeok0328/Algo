def upper_change(words) :
    change_list = []
    for word in words :
        change_list.append(word.upper())
    for i in change_list :
        print(i , end='')



upper_change('The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.')