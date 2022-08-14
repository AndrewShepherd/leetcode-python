
import unittest
from permutations_ii import Solution




class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.permuteUnique([1,1,2])
        self.assertEqual(3, len(result))

    def test_1(self):
        s = Solution()
        result = s.permuteUnique([1,2,3])
        self.assertEqual(6, len(result))

try:
    unittest.main()
except SystemExit:
    None