import unittest

from make_integer_beautiful import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, n, target, expected_result):
        sol= Solution()
        result = sol.makeIntegerBeautiful(n, target)
        self.assertEqual(result, expected_result)

    def test_3(self):
        self.run_test(16, 6, 4)

    def test_1(self):
        self.run_test(467, 6, 33)
    
    def test_2(self):
        self.run_test(99, 2, 1)

    def test_4(self):
        self.run_test(1, 1, 0)

    def test_0(self):
        self.run_test(590, 1, 410)


try:
    unittest.main()
except SystemExit:
    None













