import unittest
from min_number_of_strings_to_form_valid_target import Solution, TrieNode
import big_input

class TestSolution(unittest.TestCase):


    def test_004(self):
        words = big_input.words
        target = big_input.target
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 3)


    def test_001(self):
        words = ["abc","aaaaa","bcdef"]
        target = "aabcdabc"
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 3)

    def test_002(self):
        words = ["abababab","ab"]
        target = "ababaababa"
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 2)

    def test_003(self):
        words = ["bac","baccccacacc","babac"]
        target = "bababbbbbb"

        root = TrieNode()
        root.add_substring("bac")
        root.add_substring("baccccacacc")
        root.add_substring("babac")
        l = root.get_length('babbbbbb')
        self.assertEqual(3, l)
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 7)
        










try:
    unittest.main()
except SystemExit:
    None



















