import unittest
from find_the_k_sum_of_an_array import Solution
from large_test_case import big_list

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        result = s.kSum([2,4,-2], 5)
        self.assertEqual(2, result)

    def test_2(self):
        s = Solution()
        result = s.kSum([1,-2,3,4,-10,12], 16)
        self.assertEqual(10, result)

    def test_3(self):
        s = Solution()
        result = s.kSum([1000,1001,1002,1003,1004,1005,1006,1007,1008,1009], 10)
        self.assertEqual(9037, result)

    def test_4(self):
        s = Solution()
        result = s.kSum(big_list, 250)
        self.assertEqual(1167523899761, result)




try:
    unittest.main()
except SystemExit:
    None
