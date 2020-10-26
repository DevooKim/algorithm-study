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

    def book(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for c in s:
            if c not in table:
                stack.append(c)
            elif not stack or table[c] != stack.pop():
                return False
        return len(stack) == 0


a = Solution()
print(a.isValid("){"))