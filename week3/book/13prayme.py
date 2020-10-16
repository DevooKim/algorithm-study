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
        # while len(array_list) > 1:
        while cnt < n:
            if array_list.popleft() != array_list.pop():
                return False
            cnt += 1
        return True

    # 연결리스트에서는 반드씨 쓰이는 Runner
    # fast 덕분에 slow는 무조건 연결 리스트의 중앙에 위치한다
    def isPalindromeWithRunner(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next  # runner를 활용해서 rev에 2개씩 넣기, slow 전진시키기
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


print(Solution().isPalindrome(ListNode(val=1, next=ListNode(val=2, next=None))))
