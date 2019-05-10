'''
1)
[pencil, notebook, calculator]
[pen, laptop, lunch]

[calculator]
[pen, laptop]
[]


2a)
1
2
6
24
120

2b)
c
o
m
p
u
t
e
r

3)
a) O(n)
b) O(n)
c) O((n^2+n)/2) = O(n^2)
d) O((n^2+n)/2) = O(n^2)
'''


import copy

class Polynomial:
    def __init__(self, coef_list=None):
        self.coef_list = coef_list
        if self.coef_list == None:
            self.coef_list = []

    def __str__(self):
        if self.coef_list != []:
            polynomial = ''
            x = self.coef_list[1]
            y_intercept = self.coef_list[0]
            for i in range(len(self.coef_list)-1, 1, -1):
                if self.coef_list[i] != 0 and self.coef_list[i] != 1:
                    polynomial += str(abs(self.coef_list[i])) + 'x^' + str(i) + ' '
                    if self.coef_list[i-1] > 0:
                        polynomial += '+ '
                    elif self.coef_list[i-1] < 0:
                        polynomial += '- '
                elif self.coef_list[i] != 0:
                    polynomial += 'x^' + str(i) + ' '
                    if self.coef_list[i-1] > 0:
                        polynomial += '+ '
                    elif self.coef_list[i-1] < 0:
                        polynomial += '- '
            if x > 0:
                polynomial += '+ ' + str(abs(x)) + 'x '
            elif x < 0:
                polynomial += '- ' + str(abs(x)) + 'x '
            if y_intercept > 0:
                polynomial += '+ ' + str(abs(y_intercept))
            elif y_intercept > 0:
                polynomial += '- ' + str(abs(y_intercept))
        else:
            polynomial = '0'
        return polynomial

    def eval(self, val):
        p = 0
        for i in range(len(self.coef_list)):
            p += self.coef_list[i] * val**i
        return p

    def __add__(self, other):
        if len(self.coef_list) == 0:
            sum = other.coef_list
        elif len(other.coef_list) == 0:
            sum = self.coef_list
        elif len(self.coef_list) > len(other.coef_list):
            sum = copy.deepcopy(self.coef_list)
            for i in range(len(other.coef_list), -1, -1):
                sum[i] += other.coef_list[i]
        else:
            if len(self.coef_list) < len(other.coef_list):
                sum = copy.deepcopy(other.coef_list)
                for i in range(len(self.coef_list)-1, -1, -1):
                    sum[i] += self.coef_list[i]

        return Polynomial(sum)


p = Polynomial([3, 7, 0, -9, 2])
print(p)
m = Polynomial([3, 5, 0, 0, 8, 2, 1])
print(m)

z = p + m
print(z)

k = Polynomial()
print(k)
f = z+k
print(f)
print(f.eval(3))


def powers_of_two(num):
    count = 1
    while count < num+1:
        output = 2**count
        count += 1
        yield output


for curr_value in powers_of_two(6):
    print(curr_value)