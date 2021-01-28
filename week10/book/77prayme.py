import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter() # 빈 카운터
        for right in range(1, len(s) + 1): # 1번부터 길이 + 1
            counts[s[right - 1]] += 1 # 0~ 길이지

            max_char_n = counts.most_common(1)[0][1]

            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left


print(Solution().characterReplacement("ABAB", 2)) # 4
print(Solution().characterReplacement("AABABBA", 1)) # 4