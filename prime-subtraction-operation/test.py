import unittest
from prime_subtraction_operations import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [6,8,11,12]
        s = Solution()
        self.assertEqual(True, s.primeSubOperation(nums))

    def test_0(self):
        nums = [5,8,3]
        s = Solution()
        self.assertEqual(False, s.primeSubOperation(nums))



try:
    unittest.main()
except SystemExit:
    None










