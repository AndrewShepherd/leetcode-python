import unittest
from min_ops_to_make_array_elements_one import Solution

class TestSolution(unittest.TestCase):

    def test_0(self):
        nums = [2,6,3,4]
        output = 4
        s = Solution()
        self.assertEqual(output, s.minOperations(nums))

    def test_1(self):
        nums = [2,10,6,14]
        output = -1
        s = Solution()
        self.assertEqual(output, s.minOperations(nums))

    def test_2(self):
        nums = [48841,93382,993143,170438,48860,174356,291531]
        output = 7
        s = Solution()
        self.assertEqual(output, s.minOperations(nums))
try:
    unittest.main()
except SystemExit:
    None















