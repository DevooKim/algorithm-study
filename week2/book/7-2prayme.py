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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        elem = sorted([nums[i], nums[j], nums[k]])
                        if elem in answer:
                            break
                        answer.append(elem)
        print(f"answer: {answer}")
        return answer

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j -1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append(nums[i], nums[j], nums[k])

        return result


    # sort하면 왼쪽엔 음수 오른쪽엔 양수..
    # 맨 처음엔 중복이여도 추가하고
    # 다음부턴 중복엔 추가하지 않는다.
    # 투 포인터는 주로 정렬된 배열을 대상으로한다.
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                # 0 보다 크면 음수가 부족한거니까 왼쪽을 올린다
                if sum < 0:
                    left += 1
                # 0 보다 작으면 양수가 부족한거니까 오른쪽을 올린다.
                elif sum > 0:
                    right -= 1
                # 딱 0이면 일단 저장하고 조건에 맞게 포인터를 조절한다
                else:
                    result. append((nums[i], nums[left], nums[right]))

                    # 중복을 제거한다
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right- 1]:
                        right -= 1

                    # 중복이 없으면 양쪽 포인터를 이동한다
                    left += 1
                    right -= 1

        print(result)
        return result



Solution().threeSum3([-1, 0, 1, 2, -1, -4])
