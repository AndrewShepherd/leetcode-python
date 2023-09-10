import unittest

from min_operations import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        nums = [16, 128, 32]
        target = 1
        result = s.minOperations(nums, target)
        self.assertEqual(4, result)

    def test_0(self):
        s = Solution()
        nums = [128,1024,1073741824,4194304,268435456,1024,16,1073741824,131072,4,16777216,67108864,16777216,268435456,1073741824,256,16,67108864,1048576,16,4,4194304,1024,16,262144,1048576,1024,128,1073741824,67108864,65536,128,32768,128,32768,8192,256,1024]
        target = 38
        result = s.minOperations(nums, target)
        self.assertEqual(1, result)

    def test_5(self):
        s = Solution()
        nums = [8, 2, 64, 32]
        target = 4
        result = s.minOperations(nums, target)
        self.assertEqual(1, result)

    def test_4(self):
        s = Solution()
        nums = [1,2,8]
        target = 7
        result = s.minOperations(nums, target)
        self.assertEqual(1, result)


    def test_2(self):
        s = Solution()
        nums = [1,32,1,2]
        target = 12
        result = s.minOperations(nums, target)
        self.assertEqual(2, result)

    def test_3(self):
        s = Solution()
        nums = [1,32,1]
        target = 35
        result = s.minOperations(nums, target)
        self.assertEqual(-1, result)
    
       

try:
    unittest.main()
except SystemExit:
    None






