# https://leetcode.com/problems/reverse-prefix-of-word/description/
"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.


"""
class Solution:

  def reversePrefix(self, word: str, ch: str) -> str:
    i = word.find(ch) + 1
    return word[:i][::-1] + word[i:]

  def reversePrefix2(self, word: str, ch: str) -> str:
    i = word.find(ch) + 1
    return word[:i][::-1] + word[i:]

# a = Solution()
# Solution.reversePrefix(a, "abcd", "z")


def swap(word, idx):
    word = list(word)
    for i in range(idx//2):
        word[i], word[idx-i] = word[idx-i], word[i]

    print(word)

swap("abcde", 4)