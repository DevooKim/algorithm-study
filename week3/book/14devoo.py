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
        def append(result:ListNode, val) -> ListNode:
            result.next = ListNode(val)
            return result
        result = None
        while l1 and l2:
            if l1.val < l2.val:
                result, result.next, l1 = ListNode(l1.val), result, l1.next
            else:
                result, result.next, l2 = ListNode(l2.val), result, l2.next
                
        print(result)