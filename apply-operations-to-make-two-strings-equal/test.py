import unittest

from apply_operations import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        s1 = "1110010010010111011110100010110011101010010000101010000000101111111000100110110101110111110111110010"
        s2 = "0110010001100010110100110101110100111100101001000010001100011010101110010101000111000000110001001100"
        x = 66
        result = s.minOperations(s1, s2, x)
        self.assertEqual(52, result)

    def test_5(self):
        s = Solution()
        s1 = "101101"
        s2 = "000000"
        x = 6
        result = s.minOperations(s1, s2, x)
        self.assertEqual(4, result)

    def test_1(self):
        s = Solution()
        s1 = "1100011000"
        s2 = "0101001010"
        x = 2
        result = s.minOperations(s1, s2, x)
        self.assertEqual(4, result)

    def test_2(self):
        s = Solution()
        s1 = "10110"
        s2 = "00011"
        x = 4
        result = s.minOperations(s1, s2, x)
        self.assertEqual(-1, result)

    def test_3(self):
        s = Solution()
        s1 = "1001"
        s2 = "0000"
        x = 2
        result = s.minOperations(s1, s2, x)
        self.assertEqual(2, result)     

    def test_4(self):
        s = Solution()
        s1 = "1001"
        s2 = "0000"
        x = 4
        result = s.minOperations(s1, s2, x)
        self.assertEqual(3, result)    

try:
    unittest.main()
except SystemExit:
    None










