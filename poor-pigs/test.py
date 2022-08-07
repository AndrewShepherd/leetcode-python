import unittest
from poor_pigs import Solution

class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.poorPigs(1000, 15, 60)
        self.assertEqual(5, result)

    def test_0(self):
        s = Solution()
        result = s.poorPigs(4, 15, 15)
        self.assertEqual(2, result)

    def test_3(self):
        s = Solution()
        result = s.poorPigs(4, 15, 30)
        self.assertEqual(2, result)

    def test_4(self):
        s = Solution()
        result = s.poorPigs(1, 1, 1)
        self.assertEqual(0, result)
try:
    unittest.main()
except SystemExit:
    None