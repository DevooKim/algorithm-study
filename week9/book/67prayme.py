import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 두 배열의 교집합
        a,b  = set(nums1), set(nums2)

        answer = []
        for _a in a:
            for _b in b:
                if _a == _b:
                    answer.append(_a)
        return answer

print(Solution().intersection([1,2,2,1], [2,2]))
print(Solution().intersection([4,9,5], [9,4,9,8,4]))