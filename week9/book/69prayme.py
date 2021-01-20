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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 왼쪽에서 오른쪽 , 위에서 아래 오름차순

        row = 0
        while row < len(matrix):

            left, right = 0, len(matrix[row]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                print(matrix[row][mid])
                if matrix[row][mid] > target:
                    right = mid - 1
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    return True

            row += 1
        
        return False
    
    def book_last_element(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        row = 0
        col = len(matrix[0]) - 1

        # 크면 행을 바꾼다.
        # 작으면 열을 바꾼다.
        # 가장 마지막 보다 크면 무조건 아래 행에 있기 마련
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            
        return False

    def book_pythonic(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

case1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [10, 21, 23, 16, 30],
]

print(Solution().searchMatrix(case1, 5))