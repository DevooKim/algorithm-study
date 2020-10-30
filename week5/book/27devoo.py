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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        q = collections.deque()
        result = None
        for list in lists:
            while list:
                q.append(list.val)
                list = list.next

        q = sorted(q, reverse=True)
        for i in q:
            result, result.next = ListNode(i), result
        return result
a = Solution()