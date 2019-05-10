# The following two classes are imported from Resources at NYU Classes

class Empty(Exception):
    """
    Raised when an illegal operation is attempted on an empty Stack
    """
    pass


class Stack:
    """
    Stack implmented using a Python list
    """
    def __init__(self):
        """
        Initialize the stack with an empty Python list
        """
        self._data = []

    def __len__(self):
        """
        Size of the stack
        Delegate to the underlying Python list
        """
        return len(self._data)

    def is_empty(self):
        """
        is_empty: is the stack empty?
        """
        return len(self._data) == 0

    def push(self, item):
        """
        push: Add an element to the stack.
        Simply append it to the underlying Python list
        """
        self._data.append(item)

    def pop(self):
        """
        pop: remove the last item from the stack.
        Implement using the pop method of the Python list
        Attempting to pop an empty stack will raise an Empty exception.
        """
        if self.is_empty():
            raise Empty()
        return self._data.pop()  # list's pop returns item

    def top(self):
        """
        top: access the last item from the stack.
        Attempting to call top on an empty stack will raise an Empty exception.
        """
        if self.is_empty():
            raise Empty()
        return self._data[-1]


# actual code for problem 3

var_dict = {}                            # the dictionary with stored variables
ops = ['+', '-', '*', '/', '%']     # the operators used


def operation(x, y, operation):
    # this function performs the operation provided as a string parameter on two integer parameters
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    else:
        return x % y


def calculate(string_input):
    lst = string_input.split(" ")
    calc = Stack()
    result = ""
    for i in lst:
        try:
            # this try block attempts to push the input on the stack as an integer
            calc.push(int(i))
        except:
            # if the try fails, that means the input could either be a variable, operator, or equal
            if i in var_dict:
                calc.push(var_dict[i])
            elif i in ops:
                y = calc.pop()
                x = calc.pop()
                calc.push(operation(x, y, i))
            elif i == "=":
                result = calc.pop()
            else:
                calc.push(i)
    if result == "":
        return calc.pop()
    else:
        var_dict[result] = calc.pop()
        return result


def main():
    done = False
    while not done:
        inp = input("--> ")
        if inp != "done()":
            print(calculate(inp))
        else:
            done = True

main()
