def floorSqrt(x):
    if x == 0 or x == 1:
        return x

    l, r = 0, x//2
    ans = -1

    while l <= r:
        mid = (l+r)//2
        if mid * mid == x:
            return mid

        if mid * mid > x:
            r = mid - 1
        else:         # find first element that is smaller than x
            l = mid + 1
            ans = mid

    return ans
