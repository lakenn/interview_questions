'''
Find substring with K distinct characters
Given a string and number K, find the substrings of size K with K distinct characters.
If no, output empty list. Remember to emit the duplicate substrings, i.e. if the substring repeated twice, only output once.
'''

def check_all_diff(tokens):
    eng_map = {}

    for char in tokens:
        eng_map[char] = eng_map.get(char, 0) + 1

        if eng_map[char] > 1:
            return False

    return True


def subStringsKDist(inputStr, num):
    # WRITE YOUR CODE HERE
    total_len = len(inputStr)

    sol = {}
    for i in range(total_len):
        if i + num <= total_len:
            possible_ans = inputStr[i:i + num]

            if check_all_diff(possible_ans):
                sol[possible_ans] = 1

    return sol.keys()


subStringsKDist('awaglknagawunagwkwagl', 4)