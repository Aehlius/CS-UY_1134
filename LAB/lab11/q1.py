def most_frequent(lst):
    freq_dict = dict()
    for val in lst:
        if val not in freq_dict:
            freq_dict[val] = 1
        else:
            freq_dict[val] += 1
    max_freq = 0
    for val in freq_dict:
        if freq_dict[val] > max_freq:
            max_freq = freq_dict[val]
            max_num = val
    return max_num



if __name__ == '__main__':
    lst = [5, 9, 2, 9, 0, 5, 9, 7]
    print(most_frequent(lst))