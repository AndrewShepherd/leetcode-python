from candy import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_single(self):
        s = Solution()
        result = s.candy([1])
        self.assertEqual(1,result)

    def test_two_up(self):
        s = Solution()
        result = s.candy([1, 2])
        self.assertEqual(3,result)

    def test_two_down(self):
        s = Solution()
        result = s.candy([4, 2])
        self.assertEqual(3,result)

    def test_two_level(self):
        s = Solution()
        result = s.candy([0, 0])
        self.assertEqual(2,result)

    def test_down_then_up(self):
        s = Solution()
        result = s.candy([3, 1, 2])
        self.assertEqual(5, result)

    def test_up_then_down(self):
        s = Solution()
        result = s.candy([1, 3, 2])
        self.assertEqual(4, result)

    def test_up_one_two_down(self):
        s = Solution()
        result = s.candy([1, 4, 3, 2])
        self.assertEqual(7, result)

    def test_1(self):
        s = Solution()
        result = s.candy([1,2,2])
        self.assertEqual(4,result)
try:
    unittest.main()
except SystemExit:
    None