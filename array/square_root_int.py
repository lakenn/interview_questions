# binary search for solution
def solution(x):
    if x == 0 or x == 1:
        return x

    low = 1
    high = x//2

    while low <= high:
        mid = (low + high)//2

        square_ans = mid*mid

        if square_ans == x:
            return mid

        if square_ans > x:
            high = mid -1
        else:
            # Since we need floor, we update
            # answer when mid*mid is smaller
            # than x, and move closer to sqrt(x)
            low = mid + 1
            ans = mid

    return ans


# driver code
x = 11

print(solution(x))