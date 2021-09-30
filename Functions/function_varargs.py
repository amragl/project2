def total(a=5, *number, **phonebook):
    print('a',a)

    #Iterate through all the items in tuple
    for single_item in number:
        print('single_item',single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(10,1,2,3, Jack=1123, John=2231, Inge=1560)