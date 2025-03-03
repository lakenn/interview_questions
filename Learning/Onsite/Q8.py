"""
aabaa
"""
from itertools import groupby


def encode(plain_text):
    result = ''
    for name, group in groupby(plain_text):
        result += f'{len(list(group))}{name}'

    print(result)

def encode2(plain_text):
    if not plain_text:
        return ''

    cnt = 1
    result = ''
    for idx in range(1, len(plain_text)):
        if plain_text[idx-1] == plain_text[idx]:
            cnt += 1
        else:
            # encode previous char if encounter a diff char
            result += f'{cnt}{plain_text[idx-1]}'
            cnt = 1

    # handling remaining
    result += f'{cnt}{plain_text[-1]}'
    return result


print(encode2("aabaa"))
print(encode2("aa"))
