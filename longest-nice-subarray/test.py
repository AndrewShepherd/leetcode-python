import unittest
from longest_nice_subarray import Solution


class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.longestNiceSubarray([1,3,8,48,10])
        self.assertEqual(3, result)

    def test_0(self):
        s = Solution()
        result = s.longestNiceSubarray([3,1,5,11,13])
        self.assertEqual(1, result)

    def test_3(self):
        s = Solution()
        result = s.longestNiceSubarray([84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680])
        self.assertEqual(8, result)

    def test_4(self):
        s = Solution()
        result = s.longestNiceSubarray([1,2,4,1,8])
        self.assertEqual(4, result)

    def test_2(self):
        s = Solution()
        result = s.longestNiceSubarray([5,11])
        self.assertEqual(1, result)

try:
    unittest.main()
except SystemExit:
    None



