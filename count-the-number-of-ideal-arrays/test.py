from count_the_number_of_ideal_arrays import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_4(self):
        s = Solution()
        result = s.idealArrays(2, 5)
        self.assertEqual(10,result)

    def test_2(self):
        s = Solution()
        result = s.idealArrays(5, 3)
        self.assertEqual(11,result)

    def test_3(self):
        s = Solution()
        result = s.idealArrays(184, 389)
        self.assertEqual(510488787,result)

    def test_5(self):
        s = Solution()
        result = s.idealArrays(5878, 2900)
        self.assertEqual(465040898,result)

    def test_6(self):
        s = Solution()
        result = s.idealArrays(9767, 9557)
        self.assertEqual(465040898,result)
try:
    unittest.main()
except SystemExit:
    None