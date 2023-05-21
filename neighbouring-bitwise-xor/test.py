import unittest

from neighbouring_bitwise_xor import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        derived = [1,1,0]
        result = s.doesValidArrayExist(derived)
        self.assertEqual(True, result)

    def test_2(self):
        s = Solution()
        derived = [1,1]
        result = s.doesValidArrayExist(derived)
        self.assertEqual(True, result)

    def test_3(self):
        s = Solution()
        derived = [1,0]
        result = s.doesValidArrayExist(derived)
        self.assertEqual(False, result)
try:
    unittest.main()
except SystemExit:
    None



