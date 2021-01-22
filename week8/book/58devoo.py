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

        def arrToList(node, arr):
            if arr:
                node = ListNode(arr[0])
                node.next = arrToList(node.next, arr[1:])
            return node
        
        if not head:
            return head
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr = mergeSort(arr)

        return arrToList(ListNode(), arr)

    
    def mergedLists_book(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergedLists_book(l1.next, l2)
        return l1 or l2

    def mergeSort_book(self, head):
        if not (head and head.next):
            return head
        
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next

        half.next = None    #slow가 mid값이고 half가 slow이전이다. half 이후로 연결을 끊어버림

        l1 = self.sortList_book(head)
        l2 = self.sortList_book(slow)

        return self.mergedLists_book(l1, l2)

    def book2(self, head):
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

a = Solution()