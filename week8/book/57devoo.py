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
        self.children = collections.defaultdict(Node)

        #book
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

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

    def insert_book(self, index, word):
        node = self.root
        for i, char, in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search_book(self, index, word):
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
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
        1. word의 각 원소들을 더하여 리스트로 만든다. 
            ** 길이가 짝수인 경우만 더한다. => 반례: a, aba **
            =>  1-1. 앞 원소와 뒤 원소가 다른 경우 앞 + 뒤가 펠린드롬이면 바로 result에 추가
                1-2. 길이가 짝수인 경우 리스트에 추가한다.
        2. 1에서 만든 리스트를 trie 구조로 만든다.
        3. 리스트의 원소를 뒤집어서 trie 검색을 한다.
        4. 인덱스는 어떻게? => 별도 리스트로 관리
        '''
        lists = []
        indexs = []
        isPalindrome = []
        result = []
        trie = Trie()

        for fIdx, front in enumerate(words):
            for bIdx, back in enumerate(words):
                tmp = front + back
                if front != back:
                    if tmp == tmp[::-1]:
                        result.append([fIdx, bIdx])
                        continue
                    if len(tmp) % 2 == 0:
                        lists.append(tmp)
                        indexs.append([fIdx, bIdx])
        # print(lists)
        for word in lists:
            trie.insert(word)

        for word in lists:
            isPalindrome.append(trie.search(word[::-1]))
        
        # print(isPalindrome)
        for palindrome, idx in zip(isPalindrome, indexs):
            if palindrome:
                result.append(idx)
        return result

    def book(self, words):
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert_book(i, word)
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search_book(i, word))

        return results

        
        

a = Solution()
# print(a.palindromePairs(["abcd","dcba","lls","s","sssll"]))
# print(a.book(["abcd","dcba","lls","s","sssll"]))
# print(a.palindromePairs(["a",""]))
print(a.palindromePairs(["a","abc","aba",""]))