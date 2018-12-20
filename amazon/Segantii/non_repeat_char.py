import collections

def first_non_repeating_letter(str):
    str_list = list(str)

    hashmap = collections.OrderedDict()

    for elem in str_list:
        key = elem.lower()
        hashmap[key] = hashmap.get(key, 0) + 1

    index = '-1'
    for key, value in hashmap.items():
        if value == 1:
            index = key
            break

    if index == '-1':
        return ''

    # look for original value
    for elem in str_list:
        if index == elem.lower():
            return elem

    return index

print(first_non_repeating_letter('stress'))