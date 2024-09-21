# https://leetcode.com/problems/top-k-frequent-words

"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))  # -ve for max pq

        return [heapq.heappop(heap)[1] for _ in range(k)]
