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
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        while head:
            result, result.next, head = head, result, head.next
        return result
    
    def Recursion(self, head: ListNode) -> ListNode:
        def reverse(node: List, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head) 
a = Solution()