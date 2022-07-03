import unittest
from decode_the_message import Solution



class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")
        self.assertEqual(result, "this is a secret")

    def test_2(self):
        s = Solution()
        result = s.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
        self.assertEqual(result, "the five boxing wizards jump quickly")

try:
    unittest.main()
except SystemExit:
    None