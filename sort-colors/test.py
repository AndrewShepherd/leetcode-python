import unittest

from sort_colors import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, colors):
        sol= Solution()
        expected_result = sorted(colors)
        sol.sortColors(colors)
        self.assertEqual(colors, expected_result)

    def test_1(self):
        self.run_test([2,0,2,1,1,0])

    def test_2(self):
        self.run_test([2,0,1])

    def test_0(self):
        self.run_test([0,2,2,2,0,2,1,1])




try:
    unittest.main()
except SystemExit:
    None







