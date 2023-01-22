import unittest
from single_number import Solution



class TestSolution(unittest.TestCase):

    def test_0(self):
        nums = [2,2,3,2]
        self.assertEqual(3, Solution().singleNumber(nums))


    def test_3(self):
        nums = [0,1,0,1,0,1,99]
        self.assertEqual(99, Solution().singleNumber(nums))


try:
    unittest.main()
except SystemExit:
    None





