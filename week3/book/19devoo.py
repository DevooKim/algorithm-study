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
        rev = None
        while node:
            if size >= m and size <= n:
                rev = ListNode(node.val, rev)
                print(rev)
            node = node.next
            size += 1

