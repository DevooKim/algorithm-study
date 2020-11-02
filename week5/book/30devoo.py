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

a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("bbbbb"))