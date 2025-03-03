# Find the Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# *(Example: "abcabcbb" → Output: 3 for "abc")

def solution(A: str) -> int:
    char_set = set()
    left = 0
    result = 0

    for right in range(len(A)):
        while A[right] in char_set:
            char_set.remove(A[left])
            left += 1

        char_set.add(A[right])
        result = max(result, right - left + 1)

    return result

print(solution('abcdeafgh'))