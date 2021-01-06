import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index, word: str) -> None:
        node = self.root
        # 문자열을 뒤집어서 넣기
        for i, char in enumerate(reversed(word)):

            # palindrome이면 index를 추가하기
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            
            # 단어가 끝나면 word_id 인덱스 부여
            node = node.children[char]
            node.val = char
        node.word_id = index
        

    def search(self, word: str) -> bool:
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            # return word[::] == word[::-1]
            if len(word) == 1:
                return True

            cnt = 0
            n = len(word) // 2
            while cnt < n:
                if word.popleft() != word.pop():
                    return False
                cnt += 1
            return True
                    
        answer = []
        i = 0
        while i < len(words):
            j = i+1
            while j < len(words):
                word = collections.deque(words[i] + words[j])
                if isPalindrome(word):
                    answer.append((i,j))
                
                word = collections.deque(words[j] + words[i])
                if isPalindrome(word):
                    answer.append((j,i))
                j += 1
            i += 1

        return answer
    
    def bookPalindrome(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        output = []
        for i, word1 in enumerate(words):
            for j, words2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append((i,j))
        return output

    def book_trie(self, words: List[str]) -> List[List[int]]:
            trie = Trie()

            for i, word in enumerate(words):
                trie.insert(i, word)

            results = []
            for i, word in enumerate(words):
                results.extend(trie.search(i, word))

            return results
    





print(Solution().palindromePairs(['abcd','dcba','lls','s','sssll']))
print(Solution().palindromePairs(['bat','tab','cat']))
print(Solution().palindromePairs(["a","abc","aba",""]))