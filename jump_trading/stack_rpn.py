#!/usr/bin/env python

# an rpn calculator in python
# > 19 2.14 + 4.5 2 4.3 / - *
# [85.297441860465113]
# only supports two operands and then an operator

import operator

ops = { '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
}

max_value = 4095

def is_numeric(token):
    try:
        int(token)
        return True
    except:
        return False

def eval_expression(tokens):
    stack = []
    for token in tokens:
        #if set(token).issubset(set("0123456789.")):
        #    stack.append(float(token))
        if is_numeric(token):
            stack.append(float(token))
        elif token in ops:
            if len(stack) < 2:
                return -1
            a = stack.pop()
            b = stack.pop()
            op = ops[token]

            value = int(op(b,a))

            if value > max_value:
                return -1

            stack.append(value)
        else:
            return -1

    return stack[0]

if __name__ == '__main__':
    stack = []
    while True:
        expression = input('> ')
        if expression in ['quit','q','exit']:
            exit()
        elif expression in ['clear','empty']:
            stack = []
            continue
        elif len(expression)==0:
            continue
        stack = eval_expression(list(expression))
        print(stack)