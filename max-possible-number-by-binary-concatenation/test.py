import unittest


from max_number_by_binary_concatenation import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        nums = [6,104,15]
        result = s.maxGoodNumber(nums)
        self.assertEqual(16232, result)

    def test_5(self):
        s = Solution()
        nums = [1,18,27]
        result = s.maxGoodNumber(nums)
        self.assertEqual(1906, result)

    def test_4(self):
        s = Solution()
        nums = [2,91,119]
        result = s.maxGoodNumber(nums)
        self.assertEqual(61294, result)

    def test_3(self):
        s = Solution()
        nums = [1,11,5]
        result = s.maxGoodNumber(nums)
        self.assertEqual(221, result)

    def test_1(self):
        s = Solution()
        nums = [1,2,3]
        result = s.maxGoodNumber(nums)
        self.assertEqual(30, result)

    def test_2(self):
        s = Solution()
        nums = [2,8,16]
        result = s.maxGoodNumber(nums)
        self.assertEqual(1296, result)

try:
    unittest.main()
except SystemExit:
    None












