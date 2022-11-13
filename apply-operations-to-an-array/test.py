from apply_operations import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        result = s.applyOperations([1,2,2,1,1,0])
        self.assertEqual([1,4,2,0,0,0],result)

    def test_two(self):
        s = Solution()
        result = s.applyOperations([0,1])
        self.assertEqual([1,0],result)

try:
    unittest.main()
except SystemExit:
    None
