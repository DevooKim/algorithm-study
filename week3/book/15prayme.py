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

    def bookRecurrent(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    def bookRepeat(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev



Solution().reverseList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
)
