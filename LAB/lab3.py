'''
1)
a) 2 + 5 + 3 + 1 = 11 = c for n>=1
since 2n^4 - 4n^3 + 5n^2 + 3n + 1 < 2n^4 + 5n^4 + 3n^4 + n^4 for all n >= 1
as each individual term in the right function takes care of every positive term on left
b)  2 + 4 + 7 = 13 = c1 for n>=1
since 2n^2 + 4n + 7 < 2n^2 + 4n^2 + 7n^4
the function takes care of every term in expression individually, ensuring the right function
is always larger than left for every value grater than 1

c2 = 2 for n>=0
since 2n^2 + 4n + 7 > 2n^2 for all n>=0
adding a positive expression to a function will make it larger than the original function
if you subtract 2n^2, then 4n + 7 > 0 is proved


2) mystery([1,2,3,4,5,6,7,8,9,10])
mystery([2,3,4,5,6,7,8,9,10])
mystery([3,4,5,6,7,8,9,10])
mystery([4,5,6,7,8,9,10])
mystery([5,6,7,8,9,10])
mystery([6,7,8,9,10])
mystery([7,8,9,10])
mystery([8,9,10])
mystery([9,10])
mystery([10])
mystery([]) = 0

now that the base case is reached, the recursion runs back through the stack
so the very last val of 0 is added to i's in backwards order
since the last mystery function passes in an empty list, which results in return of
val = 0
then, every value of i is added to the variable val
producing 55

val = 10 + 0
val = 9 + 10
val = 8 + 19
val = 7 + 27
val = 6 + 34
val = 5 + 40
val = 4 + 45
val = 3 + 49
val = 2 + 52
val = 1 + 54
val = 55

'''

# problem 1

def find_lst_max(lst):
    # find the maximum integer value in list
    # without modifying the list
    curr_max = lst[0]
    if len(lst) != 1:   # ensures list has at least two values
        curr_max = find_lst_max(lst[1:])
        if curr_max < lst[0]:
            curr_max = lst[0]
    return curr_max


# test code
lst = [1,2,3,4,5,100,12,2, 200, 2, 1]
print(find_lst_max(lst))
print(lst)


# problem 2

'''
for loop runtime = n
+ operator runtime = n
since the two are nested
worst case = n*n = n^2

'''

import random

def roll_the_dice_str(n):
    # prints out an n number of dice rolls, separated by space
    rolls = []
    for i in range(n):
        rolls.append(str(random.randint(1,6)))
    s = ' '.join(rolls)
    return s


# test code
print(roll_the_dice_str(10))


# problem3

def move_zeroes(num_lst):
    # modifies the list to move all zeroes to end of list
    # without changing the order of non-zero numbers
    write_index = 0     # the index at which we will insert the index value
    for i in range(len(num_lst)):
        if num_lst[i] != 0:
            num_lst[write_index] = num_lst[i]
            write_index += 1    # for every nonzero number, the write index updates
    for i in range(write_index, len(num_lst)):
        # adds the zeroes, which are tracked using write index value
        num_lst[i] = 0
    return num_lst

# test code
print(move_zeroes([0,1,0,3,13]))
