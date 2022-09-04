import unittest
from removing_stars_from_a_string import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        s = Solution()
        result = s.removeStars("leet**cod*e")
        self.assertEqual(result, "lecoe")

    def test_1(self):
        s = Solution()
        result = s.removeStars("erase*****")
        self.assertEqual("", result)


try:
    unittest.main()
except SystemExit:
    None