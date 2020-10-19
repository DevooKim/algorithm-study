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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = ListNode()
        while l1 or l2:
            if l1.val > l2.val:
                result.val = l1.val
                result.next = None
                result = result.next
                l1 = l1.next
            elif l1.val < l2.val:
                result.val = l2.val
                result.next = None
                result = result.next
                l2 = l2.next

        if l1 is None:
            while l2:
                result.val = l2.val
                result.next = None
                result = result.next
        elif l2 is None:
            while l1:
                result.val = l1.val
                result.next = None
                result = result.next

        return result

a = Solution()