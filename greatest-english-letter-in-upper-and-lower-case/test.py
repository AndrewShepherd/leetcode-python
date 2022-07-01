from greatest_english_letter import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.greatestLetter("lEeTcOdE")
        self.assertEqual("E",result)

    def test_2(self):
        s = Solution()
        result = s.greatestLetter("arRAzFif")
        self.assertEqual("R",result)

    def test_3(self):
        s = Solution()
        result = s.greatestLetter("AbCdEfGhIjK")
        self.assertEqual("",result)
try:
    unittest.main()
except SystemExit:
    None