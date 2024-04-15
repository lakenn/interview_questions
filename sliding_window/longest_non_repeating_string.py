# https://workat.tech/problem-solving/practice/longest-substring-without-repeat

'''
s: “workattech”
Result: 6
Explanation: Longest vaild substring is “workat”.
'''
class Solution:
    def longestSubstringWithoutRepeat(self, s: str) -> int:
        # base case
        if len(s) < 2:
            return len(s)

        # to store if char is visited
        visited = [0] * 256
        max_length = 0
        left = right = 0

        # right ptr keep moving till last char
        while right < len(s):

            # if we encounter a visited char, we need to move left ptr till
            # the duplicate char become false
            if visited[ord(s[right])]:
                while visited[ord(s[right])] != False:
                    visited[ord(s[left])] = False
                    left += 1

            visited[ord(s[right])] = True
            max_length = max(max_length, right - left+1)
            right += 1

        return max_length

print(Solution().longestSubstringWithoutRepeat("workattech"))
