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
        a1, a2 = [], []
        n1, n2 = 0, 0
        while l1:
            a1.append(l1.val)
            l1 = l1.next
        while l2:
            a2.append(l2.val)
            l2 = l2.next
        
        c = 10 ** (len(a1) - 1)
        for i in a1[::-1]:
            n1 += i * c
            c /= 10
        
        c = 10 ** (len(a2) - 1)
        for i in a2[::-1]:
            n2 += i * c
            c /= 10
            
        return n1 + n2



            

a = Solution()