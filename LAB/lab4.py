# problem 1
def sum_of_nested_integers(lst):
    total = 0
    for index in range(len(lst)):
        if isinstance(lst[index], int):
            total += lst[index]
        else:
            total += sum_of_nested_integers(lst[index])
    return total


lst = [[1,2],[3,[[4],5]],6]
x = sum_of_nested_integers(lst)
print(x)


# problem 2
def find_intersection_list(lst_A, lst_B):
    index_A = 0
    index_B = 0
    intersection_list = []
    while index_A < len(lst_A) and index_B < len(lst_B):
        if lst_A[index_A] == lst_B[index_B]:
            intersection_list.append(lst_A[index_A])
            index_B += 1
            index_A += 1
        elif lst_A[index_A] < lst_B[index_B]:
            index_A += 1
        else:
            index_B += 1
    return intersection_list

lst_A = [1,6,14,15]
lst_B = [2,6,14,19]
print(find_intersection_list(lst_A,lst_B))

lst_A = [1,3,5]
lst_B = [2,4,6,8]
print(find_intersection_list(lst_A, lst_B))

lst_A = [100]
lst_B = [1,2,3,4,100]
print(find_intersection_list(lst_A, lst_B))


# problem 3
def product_evens(n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return product_evens(n-1)
    else:
        return n * product_evens(n-2)


print(product_evens(9))
print(product_evens(10))