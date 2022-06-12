from naming_a_company import Solution
from large_input import large_input
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = Solution()
        result = s.distinctNames(["coffee","donuts","time","toffee"])
        self.assertEqual(6,result)

    def test_2(self):
        s = Solution()
        result = s.distinctNames(["lack","back"])
        self.assertEqual(0,result)

    def test_1(self):
        s = Solution()
        result = s.distinctNames(large_input)
        self.assertEqual(10, result)


try:
    unittest.main()
except SystemExit:
    None