from fair_distribution_of_cookies import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        result = s.distributeCookies([8,15,10,20,8], 2)
        self.assertEqual(31,result)

    def test_2(self):
        s = Solution()
        result = s.distributeCookies([6,1,3,2,2,4,1,2], 3)
        self.assertEqual(0.25,result)

    def test_3(self):
        s = Solution()
        result = s.distributeCookies([[2,50]], 0)
        self.assertEqual(0,result)
try:
    unittest.main()
except SystemExit:
    None