from sum_of_numbers_with_units_digit_k import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.minimumNumbers(58, 9)
        self.assertEqual(2,result)

    def test_2(self):
        s = Solution()
        result = s.minimumNumbers(37, 2)
        self.assertEqual(-1,result)

    def test_3(self):
        s = Solution()
        result = s.minimumNumbers(0, 7)
        self.assertEqual(0,result)

    def test_4(self):
        s = Solution()
        result = s.minimumNumbers(2, 8)
        self.assertEqual(-1,result)

    def test_4(self):
        s = Solution()
        result = s.minimumNumbers(5, 1)
        self.assertEqual(5,result)

    def test_5(self):
        s = Solution()
        result = s.minimumNumbers(2, 8)
        self.assertEqual(-1,result)

    def test_6(self):
        s = Solution()
        result = s.minimumNumbers(10, 1)
        self.assertEqual(10, result)
try:
    unittest.main()
except SystemExit:
    None