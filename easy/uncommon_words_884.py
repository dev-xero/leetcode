import time


class Solution:
    def run(self, testcases: [[str]]):
        t1 = time.time()
        print(f"Running {len(testcases)} testcases...")

        for idx, testcase in enumerate(testcases):
            res = self.uncommonFromSentences(testcase[0], testcase[1])
            print(f'{idx+1}.', "Result =>", res)

        t2 = time.time()
        print("\nDone in", t2-t1, "seconds.")

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


def main():
    solution = Solution()
    solution.run([["this apple is sweet", "this apple is sour"]])


if __name__ == "__main__":
    main()
