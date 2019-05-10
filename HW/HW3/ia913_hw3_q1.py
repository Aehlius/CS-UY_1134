def findChange(lst01):
    # this algorithm uses the principles of binary search to find the 1
    # by modifying it to check if the previous value is 0 as opposed to a 1
    start = 0
    end = len(lst01) - 1
    while (start <= end):
        mid = (start + end) // 2
        if lst01[mid] == 1 and (mid == 0 or lst01[mid - 1] == 0):
            # the check which ensures that the 1 found is indeed the first 1
            return mid
        elif lst01[mid] == 1:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == '__main__':
    lst1 = [0, 0, 0, 0, 0, 1, 1, 1]
    print(findChange(lst1))