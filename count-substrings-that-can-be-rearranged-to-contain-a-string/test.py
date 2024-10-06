import unittest


from count_substrings_that_can_be_rearranged_to_contain_a_string import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        s = Solution()
        word1 = "bcca"
        word2 = "abc"
        result = s.validSubstringCount(word1, word2)
        self.assertEqual(1, result)

    def test_1(self):
        s = Solution()
        word1 = "abcabc"
        word2 = "abc"
        result = s.validSubstringCount(word1, word2)
        self.assertEqual(10, result)

    def test_3(self):
        s = Solution()
        word1 = "abcabc"
        word2 = "aaabc"
        result = s.validSubstringCount(word1, word2)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None












