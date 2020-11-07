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
    def numIslands(self, grid: List[List[str]]) -> int:
        # 오른쪽으로 먼저 쭉 가본다
        # 오른쪽이 0이면 왼쪽으로 이동한다.
        # 왼쪽으로 이동하면 아래를 탐색한다.
        # 방문하는 노드들은 오른쪽 아래 순서로 탐색한다.

        # 어디에 1이 있는지 어떻게 알아내야하지?
        answer = 0
        x_shape, y_shape = len(grid), len(grid[0])

        def dfs(row, col):
            if grid[row][col] != '1':
                return

            grid[row][col] = 'V'

            if row - 1 >= 0:
                dfs(row - 1, col)  # north

            if row + 1 <= x_shape - 1:
                dfs(row + 1, col)  # south

            if col - 1 >= 0:
                dfs(row, col - 1)  # west

            if col + 1 <= y_shape - 1:
                dfs(row, col + 1)  # east

        for x in range(x_shape):
            for y in range(y_shape):
                if grid[x][y] == '1':
                    dfs(x, y)
                    answer += 1

        return answer

    def book(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    count += 1
        return count


# grid의 행과 열 단위로 육지(1)인 곳을 찾아 진행한다.
# 육지를 발견하면 dfs를 호출해서 탐색을 시작한다.

# dfs는 동서남북 모두를 탐색하면서 재귀호출한다.
# 만약 육지가 아니면 바로 return으로 종료한다.
# 이렇게 재귀 호출이 백트래킹으로 모두 빠져나오면 섬 하나를 발견한 것으로 간주한다.
# 이미 방문했던 곳은 1이 아닌 값으로 마킹한다....!! (가지치기의 일종)


print(Solution().numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(Solution().numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
