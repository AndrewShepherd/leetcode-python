import unittest


from special_permutations import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()

        nums = [2,3,6]
        expected = 2 
        result = s.specialPerm(nums)
        self.assertEqual(result, expected)

    def test_1(self):
        s = Solution()

        nums = [1,4,3]
        expected = 2 
        result = s.specialPerm(nums)
        self.assertEqual(result, expected)

    def test_2(self):
        s = Solution()

        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        expected = None
        result = s.specialPerm(nums)
        self.assertLess(result, 1000000007)


try:
    unittest.main()
except SystemExit:
    None













