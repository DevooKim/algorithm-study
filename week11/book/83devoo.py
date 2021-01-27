import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. Counter
        # 2. 분할 -> 딕셔너리에 카운팅

        counter = collections.defaultdict(int)
        result = []

        def divide(arr):
            if len(arr) < 2:
                return arr
            
            mid = len(arr) // 2
            L = divide(arr[:mid])
            R = divide(arr[mid:])
            
            if L:
                counter[L[0]] += 1
            if R:
                counter[R[0]] += 1

        divide(nums)
        for c in counter:
            if counter[c] > len(nums) // 2:
                result.append(c)

        return result

    #브루트 포스
    def book1(self, nums):
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

    #다이나믹 프로그래밍
    def book2(self, nums):
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[nums] == 0:
                counts[nums] = nums.count(num)

            if counts[nums] > len(nums) // 2:
                return num

    #분할 정복
    def book3(self, nums):
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2

        a = self.book3(nums[:half])
        b = self.book3(nums[half:])

        return [b, a][nums.count(a) > half] #a가 half보다 작으면 [b,a][0]으로 b리턴 => half보다 큰 것만 리턴하게 된다.

a = Solution()
print(a.majorityElement([2,2,1,1,1,2,2]))