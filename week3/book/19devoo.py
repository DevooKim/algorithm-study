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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        size = 1
        node = head
        rev, front = None, None, None
        tmp = ListNode(head.val)
        while node and node.next:
            if size == m - 1:
                front = tmp

            if size >= m and size <= n:
                rev = ListNode(node.val, rev)
            tmp.next = ListNode(node.val, tmp)

            node = node.next
            size += 1
            
            if size == n+1:
                break

