import unittest
from max_number_of_marked_indices import Solution




class TestSolution(unittest.TestCase):


    def test_0(self):
        nums = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]
        s = Solution()
        result = s.maxNumOfMarkedIndices(nums)
        self.assertEqual(26, result)

    def test_3(self):
        nums = [3,5,2,4]
        s = Solution()
        result = s.maxNumOfMarkedIndices(nums)
        self.assertEqual(2, result)

    def test_1(self):
        nums = [9,2,5,4]
        s = Solution()
        result = s.maxNumOfMarkedIndices(nums)
        self.assertEqual(4, result)

    def test_2(self):
        nums = [7,6,8]
        s = Solution()
        result = s.maxNumOfMarkedIndices(nums)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None





