def hash(lst):
    hash_list = []
    for item in lst:
        hash = item%10
        hash_list.append(hash)
    return hash_list


if __name__ == '__main__':
    lst = [37, 47, 51, 65, 104]
    print(hash(lst))
    print(lst)