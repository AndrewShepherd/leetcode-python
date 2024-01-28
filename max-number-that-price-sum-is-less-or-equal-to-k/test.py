import unittest

from max_number import Solution, count_where_bit_is_set


class TestSolution(unittest.TestCase):


    def test_0(self):
        result = count_where_bit_is_set(5, 3)
        # (100, 101)
        self.assertEqual(2, result)

    def test_1(self):
        sol = Solution()
        k = 2
        x = 2
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(5, result)

    def test_6(self):
        sol = Solution()
        k = 4096
        x = 6
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(4127, result)

    def test_5(self):
        sol = Solution()
        k = 281
        x = 5
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(531, result)

    def test_2(self):
        sol = Solution()
        k = 9
        x = 1
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(6, result)

    def test_4(self):
        sol = Solution()
        k = 7
        x = 2
        result = sol.findMaximumNumber(k, x)
        self.assertEqual(9, result)

    def test_3(self):
        sol = Solution()
        k = 10**15
        x = 8
        result = sol.findMaximumNumber(k, x)
        # Might be right, might not be!
        self.assertEqual(343778878348159, result)

try:
    unittest.main()
except SystemExit:
    None















