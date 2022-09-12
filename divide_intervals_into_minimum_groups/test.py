import unittest


from devide_intervals_into_minimum_groups import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.minGroups(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [[5,10],[6,8],[1,5],[2,3],[1,10]],
            3
        )

    def test_2(self):
        self.run_test(
           [[1,3],[5,6],[8,10],[11,13]],
            1,
        )
try:
    unittest.main()
except SystemExit:
    None
