import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 윈도우 형식으로..

        cnt = collections.Counter(s)
        if len(cnt) == 1:
            return 1

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if s[0] == s[1]:
                return 1
            return 2

        start, window = 0, 2
        while start + window <= len(s):
            cnt = collections.Counter(s[start:start + window])

            # print(s[start:start + window])
            # print(cnt.most_common(1)[0][1])
            if cnt.most_common(1)[0][1] == 1:
                start, window = 0, window + 1
                continue

            start += 1

        return window - 1




print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3

