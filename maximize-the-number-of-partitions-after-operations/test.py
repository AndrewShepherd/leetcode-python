import unittest
import big_input

from maximumize_partitions import Solution


class TestSolution(unittest.TestCase):

    def test_4(self):
        sol = Solution()
        s = big_input.s
        k = 1
        result = sol.maxPartitionsAfterOperations(s, k)
        self.assertEqual(len(s), result)

    def test_0(self):
        sol = Solution()
        s = "abb"
        k = 1
        result = sol.maxPartitionsAfterOperations(s, k)
        self.assertEqual(3, result)

    def test_5(self):
        sol = Solution()
        s = "baac"
        k = 3
        result = sol.maxPartitionsAfterOperations(s, k)
        self.assertEqual(2, result)

    def test_2(self):
        sol = Solution()
        s = "accca"
        k = 2
        result = sol.maxPartitionsAfterOperations(s, k)
        self.assertEqual(3, result)

    def test_1(self):
        sol = Solution()
        s = "aabaab"
        k = 3
        result = sol.maxPartitionsAfterOperations(s, k)
        self.assertEqual(1, result)

    def test_3(self):
        sol = Solution()
        s = "xxyz"
        k = 1
        result = sol.maxPartitionsAfterOperations(s, k)
        self.assertEqual(4, result)

try:
    unittest.main()
except SystemExit:
    None













