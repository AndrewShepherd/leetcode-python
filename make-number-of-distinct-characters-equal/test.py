import unittest
from is_it_possible import Solution



class TestSolution(unittest.TestCase):

    def test_1(self):
        word1 = "aa"
        word2 = "ab"
        self.assertFalse(Solution().isItPossible(word1, word2))

    def test_0(self):
        word1 = "aab"
        word2 = "bccd"
        self.assertTrue(Solution().isItPossible(word1, word2))

try:
    unittest.main()
except SystemExit:
    None





