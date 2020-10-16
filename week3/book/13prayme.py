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
    def isPalindrome(self, head: ListNode) -> bool:
        array_list = collections.deque()
        while head is not None:
            array_list.append(head.val)
            head = head.next


        cnt = 0
        n = len(array_list) // 2
        while cnt < n:
            if array_list.popleft() != array_list.pop():
                return False
            cnt += 1
        return True


print(Solution().isPalindrome(ListNode(val=1, next=ListNode(val=2, next=None))))
