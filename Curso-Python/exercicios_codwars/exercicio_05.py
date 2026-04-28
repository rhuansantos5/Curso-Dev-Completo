def find_needle(haystack): 
    position = 0 

    for element in haystack:
        if element == "needle":
            break
            
        position += 1

    return f"found the needle at position {position}"

# Outra maneira de fazer o codigo

def find_needle(haystack):
    return f"found the needle at position {haystack.index("needle")}"


input_list = ["hay", "needle", "hay", "hay", "moreJunk" ,"needle"] 

print(find_needle(input_list))