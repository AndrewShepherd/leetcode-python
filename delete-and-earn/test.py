import unittest
from delete_and_earn import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.deleteAndEarn([1,1,1,2,4,5,5,5,6])
        self.assertEqual(18,result)

    def test_2(self):
        s = Solution()
        p = [12,32,93,17,100,72,40,71,37,92,58,34,29,78,11,84,77,90,92,35,12,5,27,92,91,23,65,91,85,14,42,28,80,85,38,71,62,82,66,3,33,33,55,60,48,78,63,11,20,51,78,42,37,21,100,13,60,57,91,53,49,15,45,19,51,2,96,22,32,2,46,62,58,11,29,6,74,38,70,97,4,22,76,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93]
        result = s.deleteAndEarn(p)
        self.assertEqual(3451, result)

    def test_3(self):
        s = Solution()
        p = [1,6,3,3,8,4,8,10,1,3]
        result = s.deleteAndEarn(p)
        self.assertEqual(43, result)

try:
    unittest.main()
except SystemExit:
    None