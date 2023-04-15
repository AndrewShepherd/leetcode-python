import unittest
from min_reverse_operations import Solution
import big_input

class TestSolution(unittest.TestCase):

    def test_0(self):
        n = 4
        p = 0
        banned = [1,2]
        k = 4
        output = [0,-1,-1,1]
        sol = Solution()
        self.assertEqual(output, sol.minReverseOperations(n, p, banned, k))

    def test_1(self):
        n = 5
        p = 0
        banned = [1,2]
        k = 3
        output = [0,-1,-1,-1,-1]
        sol = Solution()
        self.assertEqual(output, sol.minReverseOperations(n, p, banned, k))

    def test_3(self):
        n = 5
        p = 1
        banned = []
        k = 2
        output = [1, 0, 1, 2, 3]
        sol = Solution()
        result = sol.minReverseOperations(n, p, banned, k)
        self.assertEqual(output, result)

    def test_4(self):
        n = 4
        p = 2
        banned = []
        k = 4
        output = [-1,1,0,-1]
        sol = Solution()
        self.assertEqual(output, sol.minReverseOperations(n, p, banned, k))

    def test_big(self):
        n = big_input.n
        p = big_input.p
        banned = big_input.banned
        k = big_input.k
        output = ["todo"]
        result = Solution().minReverseOperations(n, p, banned, k)
        # The result will be very large







try:
    unittest.main()
except SystemExit:
    None















