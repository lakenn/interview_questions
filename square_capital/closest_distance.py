from typing import Iterator
import os
import sys


class NotFoundException(Exception):
    pass


def find_iter(substr: str, s: str) -> Iterator[int]:
    """
    Paste solution to part 1 here if desired
    """
    start = 0
    while True:
        start = s.find(substr, start)
        if start == -1:
            break
        yield start
        start += len(substr)


# Enter your solution in this function
def find_closest_substr_to_target(s: str, target: str, substr: str) -> int:
    target_idx = next(find_iter(target, s))

    closest_distance = sys.maxsize
    ans = -1

    substr_gen = find_iter(substr, s)

    for substr_idx in substr_gen:
        if closest_distance > abs(substr_idx - target_idx):
            closest_distance = abs(substr_idx - target_idx)
            ans = substr_idx

    if closest_distance == sys.maxsize:
        raise NotFoundException

    return ans


# These asserts should help explain what is being asked, there are actual HakcerRank test cases
# assert find_closest_substr_to_target("a b c a", "a", "b") == 2
assert find_closest_substr_to_target("target example some words example", "target", "example") == 7
assert find_closest_substr_to_target("xx t xx", "t", "xx") == 5
# Edge case where the distance between the first char of both words and target is equal, either is acceptable
assert find_closest_substr_to_target("xx ta xx", "ta", "xx") in [0, 6]
# assert find_closest_substr_to_target("target abc target", "target", "target") == 0
assert find_closest_substr_to_target("words target example test word", "target", "word") == 0
assert find_closest_substr_to_target("wordstarget example test word", "target", "word") == 0

if __name__ == '__main__':
    try:
        line = input().strip()
        result = find_closest_substr_to_target(line, "Target", "Word")
        with open(os.environ['OUTPUT_PATH'], 'w') as f:
            f.write(str(result))
    except EOFError:
        pass