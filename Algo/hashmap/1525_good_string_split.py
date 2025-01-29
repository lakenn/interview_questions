from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        left_hash = defaultdict(int)
        right_hash = defaultdict(int)

        left_hash[s[0]] += 1
        for i in range(1, len(s)):
            right_hash[s[i]] += 1

        cnt = 1 if len(left_hash.keys()) == len(right_hash.keys()) else 0

        for idx in range(1, len(s)):
            left_hash[s[idx]] += 1
            right_hash[s[idx]] -= 1
            cnt += 1 if len(left_hash.keys()) == len(right_hash.keys()) else 0

        return cnt


Solution().numSplits('aaaaa')