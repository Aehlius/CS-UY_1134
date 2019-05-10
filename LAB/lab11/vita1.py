def hash(lst):
    a = 1
    b = 2
    p = 107
    n = 14
    hash_list = []
    for item in lst:
        hash = ((a*item+b)%p)%n
        hash_list.append(hash)
    return hash_list


if __name__ == '__main__':
    lst = [37,47,51,37,65,104,8,5,10,7,8]
    print(hash(lst))
    print(lst)