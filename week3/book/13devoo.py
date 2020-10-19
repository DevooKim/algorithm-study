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

    def runner(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

a = Solution()
print(a.isPalindrome(1,2))

'''
rev = none
slow = 1 -> 2 -> 2 -> 1 -> none

rev = 1 -> 2 -> 2 -> 1 -> none
rev.next = none
=> rev = 1 -> none
slow = 2 -> 2 -> 1 -> none

rev = 2 -> 2 -> 1 -> none
rev.next = 1 -> none
=> rev = 2 -> 1 -> none
slow = 2 -> 1 -> none

rev = 2 -> 1 -> none
rev.next = 2 -> 1 -> none
=> rev =  2 -> 2 -> 1 -> none
slow = 1 -> none

rev = 1 -> none
rev.next = 2 -> 2 -> 1 -> none
=> rev = 1 -> 2 -> 2 -> 1 -> none
slow = none
'''