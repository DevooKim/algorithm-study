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

a = Solution()