import unittest

from string_indices import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        wordsContainer = ["abcd","bcd","xbcd"]
        wordsQuery = ["cd","bcd","xyz"]
        output = [1,1,1]
        result = sol.stringIndices(wordsContainer, wordsQuery)
        self.assertEqual(output, result)

    def test_2(self):
        sol = Solution()
        wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
        wordsQuery = ["gh","acbfgh","acbfegh"]
        output = [2,0,2]
        result = sol.stringIndices(wordsContainer, wordsQuery)
        self.assertEqual(output, result)


try:
    unittest.main()
except SystemExit:
    None














