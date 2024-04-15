#!/bin/python3
import os
import sys
import operator

from itertools import product

ops = { '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
}

def rpn(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ops:
            if len(stack) < 2:
                return None
            a = stack.pop()
            b = stack.pop()
            op = ops[token]
            value = int(op(b,a))
            stack.append(value)
        else:
            return None

    if len(stack) > 1:
        return None

    return stack[0]

def permutation(all_expression, variables, expression, key, value, choices):
    expression = expression.replace(key, str(value))

    choices_copy = choices.copy()

    for choice in choices_copy:
        values = variables.get(choice)
        choices_copy.remove(choice)
        permutation(all_expression, variables, expression, choice, values[0], choices_copy)
        permutation(all_expression, variables, expression, choice, values[1]-1, choices_copy)

    if len(choices) == 0:
        all_expression.append(expression)
        return

# Complete the evaluate_expression function below.
def max_result_expression(expression, variables):
    """
    Evaluates the prefix expression and calculates the maximum result
    for the given variable ranges.

    Arguments:
      expression (str): the prefix expression to evaluate.
      variables (dict): all the variables in the expression are the keys
          of this dictionary and their values are tuples `(min, max)` that
          define a range (the upper bound `max` is not included).

    Returns:
        int or None: the maximum result of the expression for any combination of the accepted
            values. If the expression is invalid, it will return `None`.
    """
    all_expressions = []
    #permutation(all_expressions, variables, expression, '', '', list(variables.keys()) )

    #https://riptutorial.com/python/example/10160/all-combinations-of-dictionary-values
    #
    # import itertools
    #
    # options = {
    #     "x": ["a", "b"],
    #     "y": [10, 20, 30]}
    #
    # keys = options.keys()
    # values = (options[key] for key in keys)
    # combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]

    #https://www.hackerrank.com/challenges/itertools-product/problem

    #https://stackoverflow.com/questions/55040080/python-create-combinations-of-dictionary
    # from itertools import product
    # D = {'a': [1, 2, 3], 'b': [0.1, 0.5], 'c': [10, 20]}
    # print([dict(zip(D.keys(), v)) for v in product(*D.values())])

    possible_range = {key: (value[0], value[1]-1) for (key,value) in variables.items()}
    all_choices = [dict(zip(variables, v)) for v in product(*possible_range.values())]

    for choice in all_choices:
        local_expression = expression
        for key in variables.keys():
            local_expression = local_expression.replace(key, str(choice.get(key)))
        all_expressions.append(local_expression)

    all_possible_results = []
    for expr in all_expressions:
        tokens = str.split(expr)
        result = rpn(reversed(tokens))

        if result is None:
            return None
        all_possible_results.append(result)

    return max(all_possible_results)

if __name__ == '__main__':
    #exp = str(input())
    #variables = eval(input())
    exp = '* + 2 x y'
    variables = eval('{"x": (0, 2), "y": (2, 4)}')
    res = max_result_expression(exp, variables)
    print(res)