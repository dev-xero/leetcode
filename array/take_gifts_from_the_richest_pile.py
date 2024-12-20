# https://leetcode.com/problems/take-gifts-from-the-richest-pile

"""
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

    Choose the pile with the maximum number of gifts.
    If there is more than one pile with the maximum number of gifts, choose any.
    Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.

Return the number of gifts remaining after k seconds.
"""

from math import sqrt, floor

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            mx = max(gifts)
            midx = gifts.index(mx)
            
            gifts[midx] = floor(sqrt(mx))

            k -= 1
        
        return sum(gifts)
        