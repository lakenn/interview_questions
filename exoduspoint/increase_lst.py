
def append(lst, val):

    idx = len(lst) - 1
    while idx > -1:
        if lst[idx] > val:
            idx -= 1
        else:
            break

    return lst[:idx + 1] + [val]


lst = []
lst = append(lst, 2)
print(lst)
lst = append(lst, 1)
print(lst)