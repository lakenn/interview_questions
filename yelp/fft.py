# http://www.smbc-comics.com/index.php?db=comics&id=2874#comic


def convert_to_base(number: int, base: int) -> [int]:
    """ Return the digits of the representation of `number` in base `base`"""

    result = []

    while number >= base:
        remainder = number % base
        result.append(remainder)
        number = number // base

    result.append(number)
    return list(reversed(result))


# print(convert_to_base(624, 8))   # [1, 1, 6, 0]
##print(convert_to_base(624, 12))  # [4, 4, 0]
# print(convert_to_base(624, 5))   # [4, 4, 4, 4]

# print(convert_to_base(-4, 2))



def fouriest_base(number: int) -> int:
    # start from base 5
    # end at base ?
    num = number
    max_result = -1
    max_resut_base = -1

    num_of_digits_base_10 = len(list(str(number)))

    for base in range(5, num+2):
        result = convert_to_base(number, base)
        print(base, result)

        if max_result >= num_of_digits_base_10:
            return max_result_base

        count = 0
        # count the number of four
        for elem in result:
            if elem == 4:
                count += 1

        if count > max_result:
            max_result = count
            max_result_base = base

    return max_result_base


print(fouriest_base(534))