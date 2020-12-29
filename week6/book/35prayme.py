import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n):
            if k > n:
                return

            for i in range(1, n):
                result.append([i, n])

            dfs(n - 1)

        result = []
        dfs(n)

        print(f'RESULT: {result}')
        return result

    def book(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result

    def book2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


print(Solution().combine(4, 2))
print(Solution().combine(1, 1))
