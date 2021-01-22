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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #x = [xL, xR], ...
        def bs(x, y):
            if x[0] < x[1] or y[0] < y[1]:
                xM = x[0] + (x[1] - x[0]) // 2
                yM = y[0] + (y[1] - y[0]) // 2

                print(xM, yM, matrix[xM][yM])
                if matrix[xM][yM] < target:
                    bs([x[0], xM], y)
                    bs(x, [y[0], yM])
                elif matrix[xM][yM] > target:
                    bs([xM, x[1]], y)
                    bs(x, [yM, y[1]])
                else:
                    return True
            return False

        return bs([0, len(matrix[0])], [0, len(matrix)])


    def book1(self, matrix, target):
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1

        return False

    def book2(self, matrix, target):
        return any(target in row for row in matrix)

a = Solution()
print(a.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 3))