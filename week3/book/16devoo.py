import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toList(arr: List, l: ListNode):
            arr.append(l.val)
            l = l.next
            return arr, l

        def toNum(arr: List) -> int:
            n = 0
            c = 10 ** (len(arr) - 1)
            for i in arr[::-1]:
                n += i * c
                c //= 10
            return n

        a1, a2 = [], []
        n1, n2 = 0, 0
        result = None
        
        while l1:
            a1, l1 = toList(a1, l1)
        while l2:
            a2, l2 = toList(a2, l2)

        n1 = toNum(a1)
        n2 = toNum(a2)
        s = str(n1 + n2)
        for i in range(len(s)):
            result, result.next = ListNode(s[i]), result
        return result

a = Solution()