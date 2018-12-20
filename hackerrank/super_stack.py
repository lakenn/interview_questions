def superStack(operations):
    stack = []

    for operation in operations:
        ops = operation.split(' ')
        instruction = ops[0]
        if instruction == 'pop':
            stack.pop()
        else:
            num = int(ops[1])


if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    operations = []
    while operations_i < operations_cnt:
        try:
            operations_item = str(input())
        except:
            operations_item = None
        operations.append(operations_item)
        operations_i += 1

    res = superStack(operations)\

        ;