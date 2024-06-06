# https://leetcode.com/problems/length-of-last-word/

class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
      i -= 1
    lastIndex = i
    while i >= 0 and s[i] != ' ':
      i -= 1

    return lastIndex - i

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        buffer = []
        last_word = 0

        for char in s:
            # flush the buffer to last word
            if char == " " and buffer:
                last_word = len(buffer)
                print(''.join(buffer))
                buffer = []
            elif char != " ":
                buffer.append(char)

        if buffer:
            last_word = len(buffer)
        return last_word
