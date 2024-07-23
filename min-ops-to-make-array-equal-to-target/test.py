import unittest

from min_ops_to_make_array_equal_to_target import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [9,2,6,10,4,8,3,4,2,3]
        target = [9,5,5,1,7,9,8,7,6,5]
        sol = Solution()
        output = sol.minimumOperations(nums, target)
        self.assertEqual(output, 20) 

    def test_3(self):
        nums = [3,5,1,2]
        target = [4,6,2,4]
        sol = Solution()
        output = sol.minimumOperations(nums, target)
        self.assertEqual(output, 2) 

    def test_2(self):
        nums = [1,3,2] 
        target = [2,1,4]
        sol = Solution()
        output = sol.minimumOperations(nums, target)
        self.assertEqual(output, 5) 






try:
    unittest.main()
except SystemExit:
    None

















