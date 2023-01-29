import unittest

from count_distinct import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, n, expected_result):
        sol= Solution()
        result = sol.distinctIntegers(n)
        self.assertEqual(result, expected_result)


    def test_1(self):
        self.run_test(5, 4)

    def test_2(self):
        self.run_test(3, 2)

    def test_3(self):
        self.run_test(1, 1)

try:
    unittest.main()
except SystemExit:
    None










