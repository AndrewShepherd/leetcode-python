import unittest
from equal_rows_and_column_pairs import Solution


class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.equalPairs(s)
        self.assertEqual(result, expectedResult)

    def test_2(self):
        self.run_test(
            [[3,2,1],[1,7,6],[2,7,7]],
            1
        )

    def test_1(self):
        self.run_test(
            [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]],
            3
        )


try:
    unittest.main()
except SystemExit:
    None
