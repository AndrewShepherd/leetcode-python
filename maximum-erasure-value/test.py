import unittest

from maximum_erasure_value import Solution


class TestSolution(unittest.TestCase):

    def run_test(self, s, exprectedResult):
        sol = Solution()
        result = sol.maximumUniqueSubarray(s)
        self.assertEqual(result, exprectedResult)

    def test_2(self):
        self.run_test([4,2,4,5,6], 17)

    def test_1(self):
        self.run_test([5,2,1,2,5,2,1,2,5], 8)

try:
    unittest.main()
except SystemExit:
    None
