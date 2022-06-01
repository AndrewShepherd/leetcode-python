import unittest
from trapping_rain_water import Solution

class TestSolution(unittest.TestCase):
    def run_test(self, input, expectedResult):
        s = Solution()
        result = s.trap(input)
        self.assertEqual(result, expectedResult)
    
    def test_one(self):
        self.run_test([0,1,0,2,1,0,1,3,2,1,2,1], 6)

    def test_two(self):
        self.run_test([4,2,0,3,2,5], 9)

try:
    unittest.main()
except SystemExit:
    None