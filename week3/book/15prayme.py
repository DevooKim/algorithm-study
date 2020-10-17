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
    pass
def reverseList(self, head: ListNode) -> ListNode:
    if not head:
        return head

    nodes = []
    while head:
        nodes.append(ListNode(head.val, None))
        head = head.next

    for i in range(len(nodes) - 1):
        nodes[i + 1].next = nodes[i]

    return nodes[-1]







Solution().reverseList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
)
