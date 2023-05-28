import unittest

from punishment_number import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        input = 10
        result = s.punishmentNumber(input)
        self.assertEqual(182, result)

    def test_2(self):
        s = Solution()
        input = 37
        result = s.punishmentNumber(input)
        self.assertEqual(1478, result)

    def test_3(self):
        s = Solution()
        input = 1000
        result = s.punishmentNumber(input)
        self.assertEqual(10804657, result)

try:
    unittest.main()
except SystemExit:
    None





