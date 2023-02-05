import unittest
from vowel_strings import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        words = ["aba","bcb","ece","aa","e"]
        queries = [[0,2],[1,4],[1,1]]
        s = Solution()
        result = s.vowelStrings(words, queries)
        self.assertEqual([2,3,0], result)


try:
    unittest.main()
except SystemExit:
    None

