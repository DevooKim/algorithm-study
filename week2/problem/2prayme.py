from typing import List


# 쿼드압축 후 개수 세기
class Solution:
    def solution(self, arr: List[List[int]]) -> int:
        result = [0, 0]
        n = len(arr)
        split = n // 2

        for i in range(0, len(arr), split):

            # y축
            for y in range(i+split-1, i-1, -1):
                print(f'i: {i} y: {y}')

            # x축
            for x in range(i, i + split):
                print(f"i: {i} x: {x}")

        # def press(self, arr):
        #     result = [0, 0]
        #     n = len(arr)
        #     split = n // 2
        #
        #     for i in range(0, len(arr), split):
        #         for j in range(i, i+split):
        #             print(f"i: {i} j: {j}")

        # result = 0
        # n = len(arr)
        # split = n // 2
        # # print(n // 2)
        #
        # for i in range(0, len(arr), split):
        #     area = arr[i][i] + arr[i][i+1] + arr[i+1][i] + arr[i+1][i+1]
        #     if area == n or area == 0:
        #         result += area
        #     else:

        return 0



Solution().solution(
    [[1, 1, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 1]]) # [4,9]

Solution().solution(
    [[1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 1, 1, 1, 1],
     [0, 1, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 1, 1]]) # [10,15]
