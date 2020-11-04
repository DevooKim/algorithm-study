import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = collections.Counter(S)

        result = 0
        for i in J:
            result += cnt[i]
        print(result)
        return result

    def book(selfself, J: str, S: str) -> int:
       return sum(s in J for s in S)

Solution().numJewelsInStones("aA", "aAAbbbb")
Solution().numJewelsInStones("z", "ZZ")