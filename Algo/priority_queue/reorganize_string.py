from collections import Counter
from heapq import heappush, heappop

# https://algo.monster/problems/reorganize_string

def reorganize_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    counter = Counter(s)

    # create a max heap of tuples (freq, char)
    heap = []
    for char, freq in counter.items():
        heappush(heap, (-freq, char))

    result = []
    prev_freq = 0
    prev_char = '#'

    while heap:
        freq1, char1 = heappop(heap)
        if not result or char1 != result[-1]:
            result.append(char1)
            freq1 += 1

        if prev_freq != 0:
            heappush(heap, (prev_freq, prev_char))

        prev_freq, prev_char = freq1, char1

    if len(result) != len(s):
        return ''

    return ''.join(result)

if __name__ == '__main__':
    s = input()
    res = reorganize_string(s)
    print(res)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i+1}")
            exit()
    print("Valid")
