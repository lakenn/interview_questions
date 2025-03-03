from itertools import groupby

"""
“aaabbcddddee” -> “a3b2c1d4e2”
“abba” -> “a1b2a1”
“a_b~~” -> “a1_1b1~2”
"""

def solution(str1):
    g = groupby(str1)
    print(g)
    for name, group in g:
        print(name, len(list(group)))

solution("aaabbcddddeeaaa")