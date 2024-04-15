# https://www.cnblogs.com/grandyang/p/8068326.html

def monotoneIncreasingDigits(N: int) -> int:
    str_n = list(str(N))
    n = len(str_n)
    j = n
    for i in range(n - 1, 0, -1):
        print(i)
        if str_n[i] >= str_n[i - 1]:
            continue
        str_n[i - 1] = str(int(str_n[i - 1]) - 1)
        j = i
    for i in range(j, n):
        str_n[i] = '9'
    return int(''.join(str_n))


print(monotoneIncreasingDigits(10))