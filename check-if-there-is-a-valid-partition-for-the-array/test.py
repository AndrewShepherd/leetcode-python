import unittest
from check_if_there_is_a_valid_partition_for_the_array import Solution




class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.validPartition([4,4,4,5,6])
        self.assertEqual(True, result)

    def test_1(self):
        s = Solution()
        result = s.validPartition([1,1,1,2])
        self.assertEqual(False, result)

    def test_2(self):
        s = Solution()
        result = s.validPartition([1,2,3])
        self.assertEqual(True, result)

    def test_3(self):
        s = Solution()
        result = s.validPartition([1,2,3,4])
        self.assertEqual(False, result)

    def test_4(self):
        s = Solution()
        result = s.validPartition([1,1,2,3,4,5,5,5])
        self.assertEqual(True, result)
 

try:
    unittest.main()
except SystemExit:
    None