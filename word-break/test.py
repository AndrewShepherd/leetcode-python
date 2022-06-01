import unittest
from word_break import Solution

class TestSolution(unittest.TestCase):
    def run_test(self, s, wordDict, expectedResult):
        sol = Solution()
        result = sol.wordBreak(s, wordDict)
        self.assertEqual(result, expectedResult)
    
    def test_1(self):
        self.run_test("leetcode", ["leet","code"], True)

    def test_two(self):
        self.run_test("applepenapple", ["apple","pen"], True)

    def test_three(self):
        self.run_test("catsandog", ["cats","dog","sand","and","cat"], False)



try:
    unittest.main()
except SystemExit:
    None