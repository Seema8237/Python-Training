no_1 = 74
no_2 = 64
no_3 = 24

if no_1 < no_2 and no_1 < no_3:
    print(F'Number 1 ({no_1}) is minimum.')


elif no_2 < no_1 <= no_3 or no_2 < no_3 <= no_1:
    print(F'Number 2 ({no_2}) is minimum.')


elif no_3 < no_1:
    if no_3 < no_2:
        print(F'Number 3 ({no_3}) is minimum.')
    else:
        print(F'Number 2 and Number 3 are same')

elif no_1==no_2==no_3:
    print("All nos. r same")

elif no_1 == no_2:
    print(F"Number 1 and Number 2 are same")

    #-----------------------------------------------------------

    """
    Looping Statement
        - For
        - while
    """

    '''
    for <iter> in <iterable_object>:
        <statement_1>
        <statement_2>
    '''
    x = ['10', 2, '3', 4, 5, 6]

    # for i in x[::2]:
    #     print(i, type(i))

    # for i in range(1, 10, 1):  #  (0, 10, 1)
    #     print(pow(2, i))
    #

    '''
    while <condition>:
        <statement_1>
        <statement_2>
    '''
    # no = 1
    # while no <= 10:
    #     print(no)
    #     no += 1

    for i in range(0, 5):
        for j in range(0, 5):
            print('*', end=" ")
        print("")