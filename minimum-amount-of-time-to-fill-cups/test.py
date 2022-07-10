import unittest


from minimum_amount_of_time_to_fill_cups import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.fillCups(s)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [1,4,2],
            4
        )

    def test_2(self):
        self.run_test(
            [5, 4, 4],
            7
        )

    def test_3(self):
        self.run_test(
            [5,0,0],
            5
        )

try:
    unittest.main()
except SystemExit:
    None
