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
    def minWindow(self, s: str, t: str) -> str:
        #딱 떠오르는 방법은 당연히 시간초과가 난다.
        #슬라이딩 윈도우에서 시간을 줄이기 힘들다
        #그러면 탐색에서 시간을 줄여야한다.
        #그걸 어떻게 하는데
        size = len(t)
        window = collections.deque
        while size <= len(s):
            for i, v in enumerate(range(len(s) - size + 1)):
                window.append(v)

    def book(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0   #아니 좀 알아보기 쉽게 씁시다. True == 1
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1

        return s[start:end]


a = Solution()
print(a.book("ADOBECODEBAANC", "AABC"))