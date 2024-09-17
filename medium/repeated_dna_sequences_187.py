import time

class Solution:
    def run(self, testcases: [str]):
        t1 = time.time()
        print(f"Running {len(testcases)} testcases...")

        for idx, testcase in enumerate(testcases):
            res = self.findRepeatedDnaSequences(testcase)
            print(f'{idx+1}.', "Result =>", res)

        t2 = time.time()
        print("\nDone in", t2-t1, "seconds.")

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


def main():
    solution = Solution()
    solution.run(["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", "AAAAAAAAAAAAA"])


if __name__ == "__main__":
    main()
