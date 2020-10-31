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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        q = collections.deque()
        result = None
        for list in lists:
            while list:
                q.append(list.val)
                list = list.next

        q = sorted(q, reverse=True)
        for i in q:
            result, result.next = ListNode(i), result
        return result

    
    def heapSolution(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
            print(heap)
        return root.next        
a = Solution()


# [(1, 0, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}), (1, 1, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}), (2, 2, ListNode{val: 2, next: ListNode{val: 6, next: None}})]
# [(1, 1, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}), (2, 2, ListNode{val: 2, next: ListNode{val: 6, next: None}}), (4, 0, ListNode{val: 4, next: ListNode{val: 5, next: None}})]
# [(2, 2, ListNode{val: 2, next: ListNode{val: 6, next: None}}), (4, 0, ListNode{val: 4, next: ListNode{val: 5, next: None}}), (3, 1, ListNode{val: 3, next: ListNode{val: 4, next: None}})]
# [(3, 1, ListNode{val: 3, next: ListNode{val: 4, next: None}}), (4, 0, ListNode{val: 4, next: ListNode{val: 5, next: None}}), (6, 2, ListNode{val: 6, next: None})]
# [(4, 0, ListNode{val: 4, next: ListNode{val: 5, next: None}}), (6, 2, ListNode{val: 6, next: None}), (4, 1, ListNode{val: 4, next: None})]
# [(4, 1, ListNode{val: 4, next: None}), (6, 2, ListNode{val: 6, next: None}), (5, 0, ListNode{val: 5, next: None})]
# [(5, 0, ListNode{val: 5, next: None}), (6, 2, ListNode{val: 6, next: None})]
# [(6, 2, ListNode{val: 6, next: None})]

# ListNode{val: None, next: None}
# ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
# ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}}
# ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 6, next: None}}}}}
# ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}}}
# ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}}}
# ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}}}}
# ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}}}}


