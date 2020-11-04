import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = -sys.maxsize
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            freq = {}
            for char in s[i:]:
                if char not in freq:
                    freq[char] = 1
                else:
                    break
            _max = max(_max, len(freq))
        return _max

    def twoPointer(self, s: str) -> int:
        used = {}
        max_len = start = 0

        for index, char in enumerate(s):
            print(used, max_len, start)
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, index - start + 1)
            used[char] = index

        return max_len

a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.twoPointer("abcabcbb"))