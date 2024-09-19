import unittest
from min_number_of_strings_to_form_valid_target import Solution, get_lps, get_backward_lengths_kmp
import big_input
import big_input_2
import big_input_3

class TestSolution(unittest.TestCase):

    def test_005(self):
        lps = get_lps("aaabaaa")
        expected = [0, 1, 2, 0, 1, 2, 3]
        self.assertEqual(lps, expected)
        self.assertEqual(get_lps("AABAACAABAA"), [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])

    def test_001(self):
        words = big_input_2.words
        target = big_input_2.target
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 10)

    def test_000(self):
        words = big_input_3.words
        target = big_input_3.target
        w = words[2][:9]
        t_small = target[49:58]
        lps = get_lps(w)
        expected = [0, 1, 0, 0, 0, 1, 2, 2, 2]
        self.assertEqual(lps, expected)

        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 824)

    def test_008(self):
        words = ["babbabbaabbaaaabb","aabababbabababbabbaaaabab","ababaa","bbaababbaabbabaaababbbaaaababbabbbabaabbaabaabaaaababaabbababaabaaabaaababaababaaabbbaaaaaabbbbaabba","baaaaabababbbbbabbbbbbabbbb","bbabaababaaabbabbbbababaababbb","bbaaababaababaabbababababbbbbbbbbbabbababbabbaaabab","aaabbabbbaababbaabbbabababaabababaaabbaaaababaaaabbabaabbbaa","bbbababaabababbbaabaaaabbbaabbabaabaaababaaabbabbaabbbabbaababbababbbbabaaabbabbbbabaaababbabbabbb","aaabbabaabbabaababbbbbaabaaabbaaaabbaaababababbbabbbbabababbaaabaabaaaabab"]
        target = "abbbaabaabaabaabaabababaaaabbbaababaababaabaaabbba"
        w = 'ababaa'

        lps = get_lps(w)
        expected_lps = [0, 0, 1, 2, 3, 1]
        self.assertEqual(lps, expected_lps)
        t_small = target[31:38]
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 12)

    def test_006(self):
        words = ["abcdef"]
        target = "xyz"
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, -1)


    def test_004(self):
        words = big_input.words
        target = big_input.target
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 3)


    def test_007(self):
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
        sol = Solution()
        output = sol.minValidStrings(words, target)
        self.assertEqual(output, 7)
        










try:
    unittest.main()
except SystemExit:
    None



















