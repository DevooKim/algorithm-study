import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 중복되는 곳 index를 탐색 그 사이의 차이가 가장 큰 수를 리턴
        hash = collections.defaultdict(int)
        result = []
        while s:
            hash[s[0]] += 1

            if len(s) == 1 and hash[s[0]] == 1:
                result.append(len(hash))
                return max(result)

            if hash[s[0]] != 1:
                result.append(len(hash))
                hash = collections.defaultdict(int)


            s = s[1:]

        return max(result)

Solution().lengthOfLongestSubstring("abcabcbb") # return 3
Solution().lengthOfLongestSubstring("bbbbb") # return 1
Solution().lengthOfLongestSubstring("pwwkew") # return 3
