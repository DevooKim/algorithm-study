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
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False

        for i in s:
            print(stack)
            if i == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif i == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif i == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                stack.append(i)

        return False if len(stack) else True


a = Solution()
print(a.isValid("){"))