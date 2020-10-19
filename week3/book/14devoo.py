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
        def append(self, result:ListNode, val) -> ListNode:
            result.next = ListNode(val)
            return result
        result = None
        while l1 and l2:
            if l1.val < l2.val:
                #result, result.next, l1 = ListNode(l1.val), result, l1.next
                if result is None:
                    result = ListNode(l1.val)
                else:
                    result = ListNode(result.val, append(result, l1.val))
                l1 = l1.next
            else:
                #result, result.next, l2 = ListNode(l2.val), result, l2.next
                if result is None:
                    result = ListNode(l2.val)
                else:
                    result = append(result, l2.val)
                
                l2 = l2.next
                
        print(result)