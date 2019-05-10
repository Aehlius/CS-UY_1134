import stack


def eval_postfix_boolean_exp(boolean_exp_str):
    expression = boolean_exp_str.split()
    num_stack = stack.Stack()
    operands = ['<', '>', '=', '&', '|']
    for value in expression:
        if value in operands:
            opr2, opr1 = num_stack.pop(), num_stack.pop()
            if value == '<' and opr1 < opr2:
                num_stack.push(True)
            elif value == '>' and opr1 > opr2:
                num_stack.push(True)
            elif value == '=' and opr1 == opr2:
                num_stack.push(True)
            elif value == '&' and opr1 == True and opr2 == True:
                num_stack.push(True)
            elif value == '|' and opr1 == True or opr2 == True:
                num_stack.push(True)
            else:
                num_stack.push(False)
        else:
            num_stack.push(value)
    return num_stack.pop()


# test code
print(eval_postfix_boolean_exp('1 2 < 6 3 < |'))