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
    def maxSubArray(self, nums: List[int]) -> int:
        #1. 전체 합을 구한다.
        #2. 순회하면서 자신을 기준으로 왼쪽과 오른쪽 합을 구한다 [a, b]
        #3. 왼쪽 합의 최소를 가진 값의 다음 부터 오른쪽 합의 최소를 가진 값까지가 결과다. (아마도)
        
        whole = sum(nums)
        part = []
        lMin, rMin = [0, sys.maxsize], [0, sys.maxsize] #[index, value]
        #[index, leftSum, rightSum]
        for i, n in enumerate(nums):
            left, right = 0, 0

            if len(part) == 0:
                left = n
                right = whole - n
                part.append([i,left, right])
            else:
                left = part[i-1][1] + n
                right = part[i-1][2] - n
                part.append([i, left, right])

            if lMin[1] > left:
                lMin = [i, left]
            if rMin[1] > right:
                rMin = [i, right]

        # return nums[lMin[0] + 1 : rMin[0] + 1]
        return sum(nums[lMin[0] + 1 : rMin[0] + 1])

    def book(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

    def book2(self, nums):
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum
a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))