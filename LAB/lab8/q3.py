def print_digits(num):

    if num == -1:
        return
    digit = num % 10
    num //= 10
    if num == 0:
        print_digits(-1)
    print(digit, end=' ')

print_digits(0)
print()