from interleaving_string import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = Solution()
        result = s.isInterleave(
            "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
            "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
            "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
        )
        self.assertFalse(result) # Don't know

    def test_1(self):
        s = Solution()
        result = s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
        self.assertTrue(result)

    def test_2(self):
        s = Solution()
        result = s.isInterleave("", "", "")
        self.assertTrue(result)

    def test_3(self):
        s = Solution()
        result = s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
        self.assertFalse(result)

try:
    unittest.main()
except SystemExit:
    None