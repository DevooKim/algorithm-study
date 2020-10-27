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
    def reverseList(self, l1: ListNode, l2: ListNode) -> ListNode:
        # list1, list2 = [], []
        # while l1 or l2:
        #     if l1:
        #         list1.append(l1.val)
        #         l1 = l1.next
        #
        #     if l2:
        #         list2.append(l2.val)
        #         l2 = l2.next
        #
        #
        # num1, num2 = 0, 0
        # square1, square2 = len(list1) - 1, len(list2) - 1
        # while list1 or list2:
        #     if list1:
        #         num1 += list1.pop() * 10 ** square1
        #         square1 -= 1
        #
        #     if list2:
        #         num2 += list2.pop() * 10 ** square2
        #         square2 -= 1
        #
        # answer = []
        # result = num1 + num2
        # # while result > 0:
        # #     answer.append(result % 10)
        # #     result //= 10
        #
        # # print(answer)
        #
        # def get(val, tail=None):
        #     if val // 10 > 0:
        #         b = ListNode(val % 10, tail)
        #         return get(val // 10, b)
        #     return ListNode(val, tail)
        #
        #
        # return get(result).toString()

        list1, list2 = [], []
        while l1 or l2:
            if l1:
                list1.append(l1.val)
                l1 = l1.next

            if l2:
                list2.append(l2.val)
                l2 = l2.next

        num1, num2 = 0, 0
        square1, square2 = len(list1) - 1, len(list2) - 1
        while list1 or list2:
            if list1:
                num1 += list1.pop() * 10 ** square1
                square1 -= 1

            if list2:
                num2 += list2.pop() * 10 ** square2
                square2 -= 1

        result = num1 + num2
        # while result > 0:
        #     answer.append(result % 10)
        #     result //= 10

        # str_result = str(result)

        result = str(result)
        a = ListNode(result[0], None)
        b = ListNode(None, None)
        for i in result[1:]:
            b = ListNode(i, a)
            a = b

        print(a.toString())
        return a


Solution().reverseList(
    ListNode(2, ListNode(4, ListNode(3, None))),
    ListNode(5, ListNode(6, ListNode(4, None)))
)
