def union_and_intersection(arr1, arr2):
    result = {}

    for elem in arr1:
        result[elem] = result.get(elem, 0) + 1

    for elem in arr2:
        result[elem] = result.get(elem, 0) + 1

    union = result.keys()
    intersection = [key for key, value in result.items() if value > 1]

    #b = list(filter(lambda v: v[1] > 1, result.items() ))

    return union, intersection

arr1 = [1,3,4,5,7]
arr2 = [2,3,5,6]

u, i = union_and_intersection(arr1, arr2)
print(1)