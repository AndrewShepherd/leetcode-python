import unittest


from sum_prefix_scores import Solution

from large_input import large_input

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.sumPrefixScores(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            ["abc","ab","bc","b"],
            [5,4,3,2]
        )

    def test_2(self):
        self.run_test(
            ["abcd"],
            [4],
        )

    def test_3(self):
        self.run_test(
            large_input,
            None
        )

try:
    unittest.main()
except SystemExit:
    None


