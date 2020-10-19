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
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        #tmp: Deque = collections.deque()
        
        while head:
            tmp.append(head.val)
            head = head.next

        #while len(tmp) > 1:
        #    if tmp.popleft() != tmp.pop():
        #        return False
        #return True

        return tmp == tmp[::-1]

a = Solution()
print(a.isPalindrome(1,2))