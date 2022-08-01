from make_array_zero_by_subtracting_equal_amounts import Solution

import unittest

class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.minimumOperations([1,5,0,3,5])
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        result = s.minimumOperations([0])
        self.assertEqual(0,result)

try:
    unittest.main()
except SystemExit:
    None