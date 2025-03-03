import bisect

list = [7,8,9,1,2,3,6,13,19,14]

list.sort(key=lambda x: x)
print(list)

idx = bisect.bisect_right(list, 5)
print(idx)