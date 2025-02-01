def sqrt(x):
    if x == 0 or x == 1:
        return x

    left, right = 1, x//2

    while left <= right:
        mid = (left + right)//2

        if mid * mid == x:
            return mid

        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right # if we need floor
    # return left # if we need ceiling

print(sqrt(8))