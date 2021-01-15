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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 일단 가장 왼쪽 인덱스가 target보다 큰지 확인
        answer = []
        for i, n in enumerate(numbers[:-1]):
            left, right = i+1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2

                two_sum = n + numbers[mid]
                if two_sum > target:
                    right = mid - 1
                elif two_sum < target:
                    left = mid + 1
                else:
                    return (i+1, mid+1)

    def book_two_pointer(self, numbers: List[int], target: int) -> List[int]:
        
        # 훨씬 빠르고 좋다
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1

    def book_bisect(self, numbers: List[int], target: int) -> List[int]:
        # 2184 밀리세컨드
        # 슬라이싱을 여러번 해서 느려짐
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k + 1:], expected)
            if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2

    def book_bisect2(self, numbers: List[int], target: int) -> List[int]:
        # 슬라이싱을 변수에 저장 후 동작하니 2배 빨라짐
        # 당연한게 슬라이싱 두번 하던걸 한번으로 줄였다.
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2

    def book_bisect3(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            # bisect.bisect_left(a, x, lo=0, hi=len(a))
            # lo는 왼쪽 범위 hi는 오른쪽 범위
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,3,4], 6))
print(Solution().twoSum([-1, 0], -1))
