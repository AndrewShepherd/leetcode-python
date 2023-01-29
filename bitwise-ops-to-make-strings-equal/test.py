import unittest
from make_strings_equal import Solution



class TestSolution(unittest.TestCase):

    def test_0(self):
        st = "1010"
        target = "0110"
        expected = True
        s = Solution()
        generated = s.makeStringsEqual(st, target)
        self.assertEqual(generated, expected)

    def test_1(self):
        st = "11"
        target = "00"
        expected = False
        s = Solution()
        generated = s.makeStringsEqual(st, target)
        self.assertEqual(generated, expected)

    def test_2(self):
        st = "11"
        target = "10"
        expected = True
        s = Solution()
        generated = s.makeStringsEqual(st, target)
        self.assertEqual(generated, expected)

    def test_3(self):
        st = "00"
        target = "11"
        expected = False
        s = Solution()
        generated = s.makeStringsEqual(st, target)
        self.assertEqual(generated, expected)

try:
    unittest.main()
except SystemExit:
    None








