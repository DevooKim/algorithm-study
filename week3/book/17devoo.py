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
a = Solution()