import heapq
import time
from collections import Counter


class Solution:
    def run(self, testcases: [[str], int]):
        t1 = time.time()
        print(f"Running {len(testcases)} testcases...")

        for idx, testcase in enumerate(testcases):
            res = self.topKFrequent(testcase[0], testcase[1])
            print(f'{idx+1}.', "Result =>", res)

        t2 = time.time()
        print("\nDone in", t2-t1, "seconds.")

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))  # -ve for max pq

        return [heapq.heappop(heap)[1] for _ in range(k)]


def main():
    solution = Solution()
    solution.run(
        [
            [["i", "love", "leetcode", "i", "love", "coding"], 2],
            [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
            [["i", "love", "leetcode", "i", "love", "coding"], 3]
        ]
    )


if __name__ == "__main__":
    main()
