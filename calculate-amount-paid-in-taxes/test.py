from calculate_amount_paid_in_taxes import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.calculateTax([[3,50],[7,10],[12,25]], 10)
        self.assertEqual(2.65000,result)

    def test_2(self):
        s = Solution()
        result = s.calculateTax([[1,0],[4,25],[5,50]], 2)
        self.assertEqual(0.25,result)

    def test_3(self):
        s = Solution()
        result = s.calculateTax([[2,50]], 0)
        self.assertEqual(0,result)
try:
    unittest.main()
except SystemExit:
    None