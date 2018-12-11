# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    N = len(S)

    phone_book_cost = {}
    phone_book_duration = {}

    lines = S.split('\n')

    for line in lines:
        parts = line.split(',')
        phone_no = parts[1]
        time = parts[0]

        # calc the cost
        hours, mins, seconds = time.split(':')

        hours = int(hours)
        mins = int(mins)
        seconds = int(seconds)

        total_seconds = hours * 60 * 60 + mins * 60 + seconds

        # smaller than 5mins
        if total_seconds < 300:
            cost = 3 * total_seconds

        else:
            total_min = hours * 60 + mins + (1 if seconds > 0 else 0)
            cost = total_min * 150

        phone_book_cost[phone_no] = phone_book_cost.get(phone_no, 0) + cost
        phone_book_duration[phone_no] = phone_book_duration.get(phone_no, 0) + total_seconds

    # max
    max_duration = max(phone_book_duration.values())

    # find all phone no with max duration
    all_phone_with_max_duration = []
    for tel, duration in phone_book_duration.items():
        if duration == max_duration:
            all_phone_with_max_duration.append(tel)

    # sort
    all_phone_with_max_duration.sort()
    free_phone_no = all_phone_with_max_duration[0]

    phone_book_cost[free_phone_no] = 0

    return sum(phone_book_cost.values())


print(solution('00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090'))


def solution(A):
    N = len(A)

    occurence = [False] * N

    for elem in A:
        print(elem)
        if occurence[elem - 1]:
            return 0
        else:
            occurence[elem - 1] = True

    if all(occ == True for occ in occurence):
        return True
    else:
        return False


print(solution([4, 1, 3, 2]))