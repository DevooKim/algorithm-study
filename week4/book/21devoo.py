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
    def removeDuplicateLetters(self, s: str) -> str:
        print(f'set(s): {set(s)}')
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            print(suffix)
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

    def stackFunc(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

a = Solution()
print(a.removeDuplicateLetters("cbacdcbc"))