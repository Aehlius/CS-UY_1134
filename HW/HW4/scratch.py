def hash(lst):
    for item in lst:
        print(item, end='  ')
        print(item%11)


if __name__ == '__main__':
    LST = [157]
    hash(LST)