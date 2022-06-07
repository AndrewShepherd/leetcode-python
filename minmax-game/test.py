import unittest


from minmax_game import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.minMaxGame(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [1,3,5,2,4,8,2,2],
            1
        )

    def test_5(self):
        self.run_test(
           [3],
            3,
        )


try:
    unittest.main()
except SystemExit:
    None
