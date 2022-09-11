import unittest
from number_of_ways import Solution




class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.numberOfWays(startPos = 1, endPos = 2, k = 3)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        result = s.numberOfWays(startPos = 2, endPos = 5, k = 10)
        self.assertEqual(0, result)

    def test_3(self):
        s = Solution()
        result = s.numberOfWays(startPos = 272, endPos = 270, k = 2)
        self.assertEqual(1, result)

    def test_4(self):
        s = Solution()
        result = s.numberOfWays(0, 10, 5)
        self.assertEqual(0, result)

    def test_0(self):
        s = Solution()
        result = s.numberOfWays(671, 669, 4)
        self.assertEqual(4, result)

try:
    unittest.main()
except SystemExit:
    None


