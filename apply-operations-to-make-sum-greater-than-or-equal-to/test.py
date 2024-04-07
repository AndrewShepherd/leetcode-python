import unittest

from min_operations import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        k = 11
        result = sol.minOperations(k)
        self.assertEqual(5, result)

    def test_2(self):
        sol = Solution()
        k = 1
        result = sol.minOperations(k)
        self.assertEqual(0, result)

    def test_3(self):
        sol = Solution()
        k = 10000
        result = sol.minOperations(k)
        self.assertEqual(198, result)       

try:
    unittest.main()
except SystemExit:
    None












