import unittest

from find_max_number_of_elements_in_subset import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        nums = [1,16,49,16,121]
        result = sol.maximumLength(nums)
        self.assertEqual(1, result)

    def test_1(self):
        sol = Solution()
        nums = [5,4,1,2,2]
        result = sol.maximumLength(nums)
        self.assertEqual(3, result)

    def test_2(self):
        sol = Solution()
        nums = [1,3,2,4]
        result = sol.maximumLength(nums)
        self.assertEqual(1, result)

    def test_3(self):
        sol = Solution()
        nums = [1,1,1,1,1,1,1,1,1,1,2,4,8,16,32,64,128,256,512,1024]
        result = sol.maximumLength(nums)
        self.assertEqual(9, result)



try:
    unittest.main()
except SystemExit:
    None
















