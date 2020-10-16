import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        if self.next is None:
            print(self.val)
        else:
            print(self.val, self.next.toString())

class Solution:
    def mergeTwoLists(self, head: ListNode) -> bool:
        def getListNode(nodes):
            if len(nodes) > 1:
                return ListNode(nodes[0], getListNode(nodes[1:]))
            elif len(nodes) == 1:
                return ListNode(nodes[0], None)

        merged = []
        while l1 or l2:
            if l1:
                merged.append(l1.val)
                l1 = l1.next
            if l2:
                merged.append(l2.val)
                l2 = l2.next

        return getListNode(sorted(merged))


print(Solution().mergeTwoLists(ListNode(val=1, next=ListNode(val=2, next=None))))