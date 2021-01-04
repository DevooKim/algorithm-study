import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Node:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.word = True

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.word

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
        1. word의 각 원소들을 더하여 리스트로 만든다. 길이가 짝수인 경우만 더한다. => 반례: a, aba
        2. 1에서 만든 리스트를 trie 구조로 만든다.
        3. 리스트의 원소를 뒤집어서 trie 검색을 한다.
        4. 인덱스는 어떻게?
        '''
        lists = []
        indexs = []
        isPalindrome = []
        result = []
        trie = Trie()

        for fIdx, front in enumerate(words):
            for bIdx, back in enumerate(words):
                # if front != back and len(front + back) % 2 == 0:
                if front != back:
                    lists.append(front + back)
                    indexs.append([fIdx, bIdx])
        print(lists)
        for word in lists:
            trie.insert(word)

        lists = [x[::-1] for x in lists]
        for word in lists:
            isPalindrome.append(trie.search(word))
        
        print(isPalindrome)
        for palindrome, idx in zip(isPalindrome, indexs):
            if palindrome:
                result.append(idx)
        return result

a = Solution()
print(a.palindromePairs(["abcd","dcba","lls","s","sssll"]))
# print(a.palindromePairs(["a",""]))