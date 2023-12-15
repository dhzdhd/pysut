from pysut import Test
import itertools as it
import time


def key(x):
    t1 = x[0]
    t2 = x[1]

    return abs(t2[0] - t1[0]) * abs(t2[1] - t1[1])


class Solution:
    @Test("examples/input2.toml")
    def maxArea(height: [int], amount: int) -> int:
        time.sleep(1)
        choices = list(it.combinations(enumerate(height), amount))
        m = max(choices, key=key)

        t1 = m[0]
        t2 = m[1]
        return abs(t2[0] - t1[0]) * abs(t2[1] - t1[1]) + 1
