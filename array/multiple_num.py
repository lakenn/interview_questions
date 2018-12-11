def solution(number):
    sum = 0

    three = 3
    five = 5

    idx = 1
    while True:
        multiple_three = idx * three
        idx += 1
        if multiple_three < number:
            sum += multiple_three

        else:
            break

    idx = 1
    while True:
        multiple_five = idx * five

        idx += 1
        if multiple_five < number:
            sum += multiple_five

        else:
            break

    return sum


print(solution(93))