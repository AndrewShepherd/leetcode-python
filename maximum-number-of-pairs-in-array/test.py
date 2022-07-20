from maximum_number_of_pairs_in_array import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = Solution()
        result = s.numberOfPairs([1,3,2,1,3,2,2])
        self.assertEqual([3,1],result)

    def test_2(self):
        s = Solution()
        result = s.numberOfPairs([1,1])
        self.assertEqual([1,0],result)

    def test_1(self):
        s = Solution()
        result = s.numberOfPairs([0])
        self.assertEqual([0, 1], result)


try:
    unittest.main()
except SystemExit:
    None