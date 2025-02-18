# https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
            You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

            A 0-indexed string num of length n + 1 is created using the following conditions:

                - num consists of the digits '1' to '9', where each digit is used at most once.
                - If pattern[i] == 'I', then num[i] < num[i + 1].
                - If pattern[i] == 'D', then num[i] > num[i + 1].

            Return the lexicographically smallest possible string num that meets the conditions.
        """
        def buildSequence(curr_idx, curr_count):
            if curr_idx != len(pattern):
                if pattern[curr_idx] == 'I':
                    buildSequence(curr_idx + 1, curr_idx + 1)
                
                else:
                    curr_count = buildSequence(curr_idx + 1, curr_count)
            
            
            self.result.append(str(curr_count + 1))
            
            return curr_count + 1

        
        self.result = []
        buildSequence(0, 0)

        return "".join(self.result[::-1])
        