import unittest

from apply_ops import Solution


class TestSolution(unittest.TestCase):

    def test_3(self):
        s = Solution()
        nums = [79170,82198,930,79685,85470,53820,93210,93840,12420,81713,187,67830,59182,92820,58938,28438,36037,1,44531,87780,84550,19654,7719,94094,1,46198,13940,80370,20370,38454,2730,3949,1,57679,11910,79170,1,71655,42442,77713,67901,52029,62790,98175,51576,31155,72939,2864,45045,1,94710,98271,9049,68556,53130,1,96328,1,35550,1]
        k = 1301
        result = s.maximumScore(nums, k)
        self.assertEqual(171781892, result) 

    def test_0(self):
        s = Solution()
        nums = [8,3,9,3,8] 
        k = 2
        result = s.maximumScore(nums, k)
        self.assertEqual(81, result)


    def test_2(self):
        s = Solution()
        nums = [19,12,14,6,10,18] 
        k = 3
        result = s.maximumScore(nums, k)
        self.assertEqual(4788, result)   

    def test_1(self):
        s = Solution()
        nums = [3289,2832,14858,22011]
        k = 6
        result = s.maximumScore(nums, k)
        self.assertEqual(256720975, result)   
       
try:
    unittest.main()
except SystemExit:
    None







