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
    answer: int = 0
    def search(self, nums: List[int], target: int) -> int:
        # 정렬이 되어 있는 상태다.
        def binary_search(arr: List[int]):
            middle = len(arr)//2
            self.answer += middle
            if middle == 0:
                # print(arr)
                if arr[0] == target:
                    return self.answer
                return -1

            if arr[middle] == target:
                return self.answer
            elif arr[middle] < target:
                return binary_search(arr[middle:])
            elif arr[middle] > target:
                return binary_search(arr[:middle])

        return binary_search(nums)
    
    def book(self, nums:List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left+right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1
            
        return binary_search(0, len(nums) - 1)
            






print(Solution().search([-1,0,3,5,9,12], 9))

