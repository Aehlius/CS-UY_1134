'''
Stack class implementation
Uses Python list
'''


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


def balanced(seq):
    """
    balanced: check if the 'braces' are balanced.
    Handles parentheses, curly braces and sqaure brackets
    """
    openBrace = '({['
    closeBrace = ')}]'
    braceStack = Stack()
    for item in seq:
        # Remember the open braces
        if item in openBrace:
            braceStack.push(item)
        elif item in closeBrace:
            # if the top item on the stack doesn't correspond to the closing 
            # brace then we have failed.
            if braceStack.is_empty():
                return False
            if openBrace.index(braceStack.top()) != closeBrace.index(item):
                return False
            braceStack.pop()
    # When we are done with the input, there better not be any unmatched braces
    # still on the stack
    return braceStack.is_empty()


def postfix(seq):
    """
    Exectue a postfix expression
    """
    s = Stack()
    for item in seq:
        #  All operations get handled by popping off the appropriate number
        #  of operands and processing them.
        #  If there aren't enough operands present, the stack will be empty
        #  and an Empty exception will be raised.  Probably cleaner if we
        #  raised our own exception.
        if item == '+':
            s.push(s.pop()+s.pop())
        elif item == '-':
            rhs = s.pop()
            lhs = s.pop()
            s.push(lhs-rhs)
        elif item == '*':
            s.push(s.pop()*s.pop())
        elif item == '/':
            rhs = s.pop()
            lhs = s.pop()
            s.push(lhs/rhs)
        else:
            # if it wasn't an operator, then it must be an operand.  Just add
            # it to the stack
            s.push(item)
    # The result should be on the top of the stack.
    # Actually it would be an error if there is more than one item there
    # but we aren't checking
    return s.pop()

def postfix2(seq):
    s = Stack()
    for item in seq:
        if item in "+-/*":
            rhs, lhs = s.pop(), s.pop()
            if item == '+':
                s.push(lhs + rhs)
            elif item == '-':
                s.push(lhs - rhs)
            elif item == '*':
                s.push(lhs * rhs)
            elif item == '/':
                s.push(lhs / rhs)
        else:
            s.push(item)
    return s.pop()

def infix_to_postfix(seq):
    """
    Convert an infix expression to postfix
    """
    ops = ['+', '-', '*', '/']
    opStack = Stack()
    post = []
    for item in seq:
        if item in ops:
            opStack.push(item)
        elif item == '(':
            opStack.push(item)
        elif item == ')':
            op = opStack.pop()
            while op != '(':
                post.append(op)
                op = opStack.pop()
        else:
            post.append(item)
    while not opStack.is_empty():
        op = opStack.pop()
        post.append(op)
    return post


def infixString_to_postfix(s):
    """
    Convert an infix string to a postfix expression.
    """
    notNum = ['+', '-', '*', '/', '(', ')']
    seq = []
    for item in s.split():
        if item not in notNum:
            item = int(item)
        seq.append(item)
    return infix_to_postfix(seq)


if __name__ == '__main__':
    print('================')
    import sys
    # Test basic stack
    s = Stack()
    print(s.is_empty())

    # How much space is used by our stack as it grows?
    for i in range(100):
        s.push(i)
        print(s.top(), sys.getsizeof(s._data))

    print('================')
    # How much space is used by our stack as it shrinks?
    while not s.is_empty():
        print(s.pop(), sys.getsizeof(s._data))
    print('================')
    
    # Test paren balancing
    balanced('([]{})')
    balanced('([]{}[)])')
    balanced('(')
    balanced(')')

    print('================')
    # Test postfix
    print(postfix([1, 2, '+', 10, '-', 2, 3, '+', '*']))

    # Test infix to postfix conversion
    print(infix_to_postfix([1, '+',  2]))
    print(infixString_to_postfix('1 + 2'))

    print(infixString_to_postfix('1 + 2 * 3'))
    print(infixString_to_postfix('1 * 2 + 3')) # not supporting precedence
    print(postfix(infixString_to_postfix('1 + 2 * 3')))
    print(postfix(infixString_to_postfix('( 1 + 2 ) * 3')))    
    print(postfix(infixString_to_postfix('1 + ( 2 * 3 )')))
    
