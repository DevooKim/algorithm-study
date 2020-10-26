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
        stack = []
        s = sorted(s)
        result = ""
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] != c:
                    result += stack.pop()
                    stack.append(c)
        result += stack.pop()
        return result

a = Solution()
print(a.removeDuplicateLetters("cbacdcbc"))