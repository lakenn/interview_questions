import math

def finalInstances(instances, averageUtil):
    # Write your code here
    i = 0
    cnt = instances

    while i < len(averageUtil):
        avg_util = averageUtil[i]
        # scale down
        if avg_util < 25 and cnt > 1:
            cnt = math.ceil(cnt/2)
            i += 11
        elif avg_util > 60:
            cnt *= 2
            i += 11
        i += 1

    return cnt


if __name__ == '__main__':
    instances = 5
    averageUtil = [6,30,5,4,8,19,89]
    print(finalInstances(instances, averageUtil))