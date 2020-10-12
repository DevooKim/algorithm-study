from typing import List


# 쿼드압축 후 개수 세기
class Solution:
    def solution(self, arr: List[List[int]]) -> int:
        return answer


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
