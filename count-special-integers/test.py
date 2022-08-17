import unittest


from count_special_integers import Solution

class TestSolution(unittest.TestCase):

    def test_7(self):
        s = Solution()
        self.assertEqual(11, s.countSpecialNumbers(12))

    def test_6(self):
        s = Solution()
        self.assertEqual(19, s.countSpecialNumbers(20))

    def test_2(self):
        s = Solution()
        self.assertEqual(5, s.countSpecialNumbers(5))
    
    def test_3(self):
        s = Solution()
        self.assertEqual(110, s.countSpecialNumbers(135))

    def test_1(self):
        s = Solution()
        self.assertEqual(178, s.countSpecialNumbers(225))

    def test_5(self):
        s = Solution()
        self.assertEqual(178, s.countSpecialNumbers(219))

    def test_8(self):
        s = Solution()
        self.assertEqual(309, s.countSpecialNumbers(403))

    def test_0(self):
        s = Solution()
        self.assertEqual(5459850, s.countSpecialNumbers(951797715))

try:
    unittest.main()
except SystemExit:
    None
