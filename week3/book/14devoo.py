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
        result = None
        while l1 and l2:
            if l1.val < l2.val:
                result, result.next, l1 = ListNode(l1.val), result, l1.next
            else:
                result, result.next, l2 = ListNode(l2.val), result, l2.next
                
        if l1 is None:
            while l2:
                result, result.next, l2 = ListNode(l2.val), result, l2.next
        elif l2 is None:
            while l1:
                result, result.next, l1 = ListNode(l1.val), result, l1.next

        rev = None
        while result:
            rev, rev.next, result = result, rev, result.next
        return rev

    def Recursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1