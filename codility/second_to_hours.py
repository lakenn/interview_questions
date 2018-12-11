def solution(T):
    # write your code in Python 3.6
    hours = int(T / 3600)
    mins = int((T - hours * 3600) / 60)
    seconds = T - hours * 3600 - mins * 60

    result = "{}h{}m{}s".format(hours, mins, seconds)

    return result

print(solution(3661))