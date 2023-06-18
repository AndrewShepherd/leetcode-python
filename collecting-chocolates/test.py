import unittest


from collecting_chocolates import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()

        nums = list(range(1000))
        x = 500
        expected = 374750 # Don't know
        result = s.minCost(nums, x)
        self.assertEqual(result, expected)

    def test_2(self):
        s = Solution()

        nums = [20,1,15]
        x = 5
        expected = 13
        result = s.minCost(nums, x)
        self.assertEqual(result, expected)

    def test_1(self):
        s = Solution()

        nums = [1,2,3]
        x = 4
        expected = 6
        result = s.minCost(nums, x)
        self.assertEqual(result, expected)


try:
    unittest.main()
except SystemExit:
    None












