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
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(lists):
            if len(result) == target_length:
                return

            print(f'LISTS: {lists}')
            result.append(lists)
            head = lists[:1]
            tail = lists[1:]
            for i in range(len(lists[1:]) - 1):
                tail = tail[1:] + tail[:1]
                result.append(head + tail)
            print(f'HEAD: {head}')
            print(f'TAIL: {tail}')
            print(f'TAIL + HEAD: {tail + head}')
            dfs(lists[1:] + lists[:1])

        target_length = 1
        for i in range(2, len(nums) + 1):
            target_length *= i

        result = []
        dfs(nums)

        return result

    def book(self, nums: List[int]) -> List[List[int]]:
        # 레벨이 증가할수록 자식 노드의 개수는 점점 작아진다.
        # 최상위는 자식노드 3개 -> 2개 -> 1개
        # 팩토리얼과 같다. 리스트의 길이가 5개였으면 5 -> 4 -> 3 -> 2 -> 1

        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                print(f'NEXT_ELEM: {next_elements}')

                prev_elements.append(e)
                print(f'PREV_ELEM: {prev_elements}')
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result

    def book2(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

    def retry(self, nums: List[int]) -> List[List[int]]:

        clone_list, clone = [], nums[1::]
        clone_list.append(clone)
        for i in range(len(clone) - 1):
            clone_list.append(clone[1:] + clone[:1])

        result = []
        for e in clone_list:
            for i in range(len(nums)):
                element = e[::]
                element.insert(i, nums[0])
                result.append(element)

        return result



# print(Solution().permute([1, 2, 3]))
print(Solution().retry([1, 2, 3]))

# [[5, 4, 6, 2], [5, 6, 2, 4], [5, 2, 4, 6], [4, 6, 2, 5], [4, 2, 5, 6], [4, 5, 6, 2], [6, 2, 5, 4], [6, 5, 4, 2],
#  [6, 4, 2, 5], [2, 5, 4, 6], [2, 4, 6, 5], [2, 6, 5, 4], [5, 4, 6, 2], [5, 6, 2, 4], [5, 2, 4, 6], [4, 6, 2, 5],
#  [4, 2, 5, 6], [4, 5, 6, 2], [6, 2, 5, 4], [6, 5, 4, 2], [6, 4, 2, 5], [2, 5, 4, 6], [2, 4, 6, 5], [2, 6, 5, 4]]
# #
# [[5, 4, 6, 2], [5, 4, 2, 6], [5, 6, 4, 2], [5, 6, 2, 4], [5, 2, 4, 6], [5, 2, 6, 4], [4, 5, 6, 2], [4, 5, 2, 6],
#  [4, 6, 5, 2], [4, 6, 2, 5], [4, 2, 5, 6], [4, 2, 6, 5], [6, 5, 4, 2], [6, 5, 2, 4], [6, 4, 5, 2], [6, 4, 2, 5],
#  [6, 2, 5, 4], [6, 2, 4, 5], [2, 5, 4, 6], [2, 5, 6, 4], [2, 4, 5, 6], [2, 4, 6, 5], [2, 6, 5, 4], [2, 6, 4, 5]]