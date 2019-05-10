# problem 5 - generator

import math


def factors(num):
    """This function yields factors of a number in an increasing order"""
    lst_factors = []
    if math.sqrt(num) == int(math.sqrt(num)):
        # check if the number has an integer square root
        # if it does, the list of factors starts one integer ahead
        # in order to avoid double factors
        middle_value_index = 2
    else:
        middle_value_index = 1
    for i in range(1, int(math.sqrt(num))+1):
        if num%i == 0:
            lst_factors.append(i)
            yield str(i) + ' '
    for reverse_index in range(len(lst_factors)-middle_value_index, -1, -1):
        # the range starts with a different number depending on whether
        # num passed has integer square roots
        # in order to make sure only one square root factor is in
        # the final answer
        yield int(num/lst_factors[reverse_index])


# TEST CODE
for curr_factor in factors(100):
    print(curr_factor)


# problem 6 - OOP

"""
This is based on Goodrich's vector.py. Most changes
are just formatting. And using an occasional better name.
"""


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        """
        d is either the dimensionality of the space
        or a sequence of coordinates
        """
        if isinstance(d, int): self._coords = [0] * d
        else:
            try:
                # Allowing any form of iterable for d
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, index):
        """Return jth coordinate of vector."""
        return self._coords[index]

    def __setitem__(self, index, val):
        """Set jth coordinate of vector to given value."""
        self._coords[index] = val

    def __add__(self, other):
        """Return sum of two vectors. Assuming they have the same dimension"""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for index in range(len(self)):
            result[index] = self[index] + other[index]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

    def __lt__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords

    def __sub__(self, other):
        """Return difference of two vectors. Assuming they have the same dimension"""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for index in range(len(self)):
            result[index] = self[index] - other[index]
        return result

    def __neg__(self):
        """Return the negative of a vector"""
        result = Vector(len(self))  # start with vector of zeros
        for index in range(len(self)):
            result[index] = - self[index]
        return result

    def __radd__(self, other):
        """Return sum of vector and class vector, where vector class comes after operand"""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for index in range(len(self)):
            result[index] = self[index] + other[index]
        return result

    def __mul__(self, other):
        """Return the multiplication of a vector class with another vector or a scalar"""
        if isinstance(other, int):  # if other is a scalar, then scalar multiplication is performed
            result = Vector(len(self))  # start with vector of zeros
            for index in range(len(self)):
                result[index] = self[index]*other
            return result
        else:   # otherwise, the other is a vector, and thus dot product is found
            if len(self) != len(other):  # relies on __len__ method
                raise ValueError('dimensions must agree')
            total = 0
            result = Vector(len(self))  # start with vector of zeros
            for index in range(len(self)):
                # the loop multiplies every corresponding vector value
                result[index] = self[index] * other[index]
            for elem in result:
                # and this loop adds up all individual values
                total += elem
            return total

    def __rmul__(self, other):
        """Return the multiplication of a vector class with a vector or a scalar, where vector class is after operand"""
        if isinstance(other, int):
            result = Vector(len(self))  # start with vector of zeros
            for index in range(len(self)):
                result[index] = self[index]*other
            return result
        else:
            if len(self) != len(other):  # relies on __len__ method
                raise ValueError('dimensions must agree')
            total = 0
            result = Vector(len(self))  # start with vector of zeros
            for index in range(len(self)):
                result[index] = self[index] * other[index]
            for elem in result:
                total += elem
            return total


# TEST CODE
def main():
    u = Vector([5, 10, 15])
    z = [5, 10, 15] + u
    print(z)
    x = z - u
    print(x)
    c = - u
    print(c)
    o = 3*c
    p = c*3
    print(o, p)

    vec1 = Vector([1, 2, 3])
    vec2 = Vector([4, 5, 6])
    print("subtraction method")
    print(vec1 - vec2)
    print("")
    print("unary method")
    print(-vec1)
    print("")
    print("addition method")
    print([1, 2, 3] + vec2)
    print("")
    print("scalar multiplication")
    print(vec1 * 4)
    print("")
    print("reverse scalar multiplication")
    print(4 * vec1)
    print("")
    print("dot multiplication")
    print(vec1 * vec2)


if __name__==__main__:
    main()