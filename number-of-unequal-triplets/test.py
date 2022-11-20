import unittest

from number_of_unequal_triplets import Solution



class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        result = s.unequalTriplets( [4,4,2,4,3])
        self.assertEqual(3, result)

    def test_1(self):
        s = Solution()
        result = s.unequalTriplets([1,1,1,1,1])
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None








