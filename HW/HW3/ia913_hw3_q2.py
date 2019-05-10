def find_duplicates(lst):
    lst_of_duplicates = []
    # constant work, initializing an empty list
    integer_lst = [0] * (len(lst))
    # initializing a list of len n and filling it with zeroes, O(n) amortized work
    for i in range(len(lst)):
        # looping n times, doing constant amount of work every loop by changing a value in list
        integer_lst[lst[i]] += 1
    for i in range(len(integer_lst)):
        # looping n times again doing 1 piece of work to compare and O(1) amortized pieces of work to append
        if integer_lst[i] > 1:
            lst_of_duplicates.append(i)
    return lst_of_duplicates


"""
The total amount of work is thus 1 + n amortized + n + 
2n amortized in worst case (if you check every single value and have to append it to duplicate list)
= 4n + 1 amortized = O(n) still linear implementation
"""

if __name__ == '__main__':
    lst = [2, 4, 4, 1, 2]
    print(find_duplicates(lst))
