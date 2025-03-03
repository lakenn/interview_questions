from concurrent.futures import ThreadPoolExecutor


def print_task(num):
    print(num)

with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(print_task, [1, 3, 44])

