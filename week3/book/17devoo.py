import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        swp = head
        while swp and swp.next:
            swp.val, swp.next.val = swp.next.val, swp.val
            swp = swp.next.next
        return head

    def swap(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next

    def Recursion(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.Recursion(p.next)
            p.next = head
            return p
        return head