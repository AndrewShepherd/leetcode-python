import unittest

from total_characters_in_string_after_transformations_ii import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = "abcyy"
        t = 2
        nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
        sol = Solution()
        result = sol.lengthAfterTransformations(s,t,nums)
        self.assertEqual(result, 7)

    def test_2(self):
        s = "azbk"
        t = 1
        nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        sol = Solution()
        result = sol.lengthAfterTransformations(s,t,nums)
        self.assertEqual(result, 8)

    def test_3(self):
        s = "x"
        t = 16
        nums = [6,6,8,1,9,9,10,3,9,4,8,5,2,8,10,2,6,8,2,3,3,7,2,6,4,2]
        sol = Solution()
        result = sol.lengthAfterTransformations(s,t,nums)
        self.assertEqual(result, 417796858)









try:
    unittest.main()
except SystemExit:
    None



















