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
    def largestNumber(self, nums: List[int]) -> str:
        '''
        0. 정렬하고 시작(?) 작은 자리수가 앞쪽에 위치해야한다.
        1. 자리수를 기준으로 정렬(키: 앞 자리수)
            1.1 높은 자리수부터 낮은 자리 수 까지 반복
            1.2 성능 향상을 위해 원소의 자리수가 키의 자리수 이상일 경우만 정렬
        '''

        def split(num):
            count = 0

            while num >= 10:
                num //= 10
                count += 1
            return count, num

        for n in nums:
            print(split(n), n)



    def comp(self, n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)

    def Book(self, nums):
        i = 1
        for i in range(1, len(nums)):
            prev = i
            while prev > 0 and self.comp(nums[prev-1], nums[prev]):
                nums[prev], nums[prev-1] = nums[prev-1], nums[prev]
                prev -= 1
        return nums
a = Solution()
# print(a.largestNumber([3, 30, 34, 100, 102, 307, 9301, 91]))
print(a.Book([3, 30, 34, 5, 9]))