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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def recurrent(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1 # l1 과 l2를 비교해서 작은 값이 왼쪽에 오게 한다.
        if l1:
            l1.next = self.recurrent(l1.next, l2)
        return l1




Solution().mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4, None))),
    ListNode(1, ListNode(3, ListNode(4, None)))
)

