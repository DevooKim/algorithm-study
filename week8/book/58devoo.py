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
    def sortList(self, head: ListNode) -> ListNode:

        def mergeSort(arr):
            if len(arr) < 2:
                return arr

            mid = len(arr) // 2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []

            while left and right:
                if left[0] < right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))

            if left:
                merged += left
            if right:
                merged += right

            return merged

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return mergeSort(arr)

a = Solution()