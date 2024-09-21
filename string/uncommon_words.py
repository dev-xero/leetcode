# https://leetcode.com/problems/uncommon-words-from-two-sentences

"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        uncommon = []
        ws1 = s1.split(" ")
        ws2 = s2.split(" ")

        for word in ws1:
            if ws1.count(word) == 1 and ws2.count(word) == 0:
                uncommon.append(word)

        for word in ws2:
            if ws2.count(word) == 1 and ws1.count(word) == 0:
                uncommon.append(word)

        return uncommon
