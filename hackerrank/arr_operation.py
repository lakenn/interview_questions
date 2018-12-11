import os

def listMax(n, operations):
    # Write your code here
    arr = [0] * n
    print(operations)

    for operation in operations:
        start = operation[0]
        end = operation[1]
        num = operation[2]

        for i in range(start-1, end):
            arr[i] += num

    return max(arr)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    operations_rows = int(input().strip())
    operations_columns = int(input().strip())

    operations = []

    for _ in range(operations_rows):
        operations.append(list(map(int, input().rstrip().split())))

    result = listMax(n, operations)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()