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
    
    def intersection_bisect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 이진 탐색을 쓰기 위해서 일단 정렬하자
        longer, shorter = [], []
        if len(nums1) >= len(nums2):
            longer, shorter = set(nums1), set(nums2)
        else:
            longer, shorter = set(nums2), set(nums1)

        longer = list(longer)
        longer.sort()


        answer = []
        for i in set(shorter):
            left, right = 0, len(longer) - 1
            while left <= right:
                mid = left + (right - left) // 2

                if longer[mid] < i:
                    left = mid + 1
                elif longer[mid] > i:
                    right = mid - 1
                else:
                    answer.append(i)
                    break
        return answer

    def book_bisect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            print(i2)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result

    def book_two_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1.sort()
        nums2.sort()

        i = j = 0

        # 각각 정렬에 O(n logN) 씩 / 비교에 O(2n)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result


print(Solution().book_bisect([1,2,2,1], [2,2]))
print(Solution().book_bisect([4,9,5], [9,4,9,8,4]))