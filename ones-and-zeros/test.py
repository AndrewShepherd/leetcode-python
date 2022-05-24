import unittest


from ones_and_zeros import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, strs, m, n, expectedResult):
        sol= Solution()
        result = sol.findMaxForm(strs, m, n)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            ["10","0001","111001","1","0"],
            5,
            3,
            4
        )

    def test_2(self):
        self.run_test(
            ["10","0","1"],
            1,
            1,
            2
        )

try:
    unittest.main()
except SystemExit:
    None
