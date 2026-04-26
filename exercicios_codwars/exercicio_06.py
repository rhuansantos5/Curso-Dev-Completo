def invert(lst):
    invert_list = []
    
    for item in lst:
        inverted_item = item * -1
        invert_list.append(inverted_item)
    
    return invert_list

itens  = [1, 2, 3, 4, 5]

print(invert(itens))


# def make_negative( number ):
    # if number > 0:
    #     return number * -1
    # return number 
    
