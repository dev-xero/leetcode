# https://leetcode.com/problems/repeated-dna-sequences

"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        freq_map = {}
        sequences = []

        for curr in range(len(s) - 9):
            sequence = s[curr:curr+10]
            if sequence in freq_map:
                if freq_map[sequence] == 1:
                    sequences.append(sequence)
                freq_map[sequence] += 1
            else:
                freq_map[sequence] = 1

        return sequences
