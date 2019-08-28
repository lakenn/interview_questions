#https://github.com/hongj77/coding-practice/commits
''' You are given a library with n words (w[0], w[1], ..., w[n-1]). You choose a word from it and
	each step, remove one letter only if doing so yields another word in the library. What is the
	longest possible chain of these removal steps? '''


def differByOne(word1,word2):
    subsequence = True
    for c in word1:
        if c not in word2:
            subsequence = False
            break
    return subsequence

# 1d DP
def solution(words):
    sol = [1] * len(words)

    # sort the words according to len
    words.sort(key=lambda s: len(s))

    # for each word
    for i in range(len(words)):
        # look up previous level
        for j in range(i):
            if len(words[i]) - len(words[j]) == 1:
                if differByOne(words[j], words[i]):
                    sol[i] = max(sol[j] + 1, sol[i])

    return max(sol)


if __name__ == '__main__':
    a = ["a", "b", "ba", "bca", "bda", "bdff"]  # longest chain is 4
    print(solution(a))