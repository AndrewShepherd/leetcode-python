import unittest

from palindrome_pairs import Solution
import large_testcase

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.palindromePairs(input)
        self.assertEqual(sorted(result), sorted(expectedResult))

    def test_0(self):
        sol= Solution()
        result = sol.palindromePairs(large_testcase.large_dataset)

    def test_5(self):
        self.run_test(
            ["a", "aba"],
            []
        )

    def test_1(self):
        self.run_test(
            ["abcd","dcba","lls","s","sssll"],
            [[0,1],[1,0],[3,2],[2,4]]
        )

    def test_2(self):
        self.run_test(
            ["bat","tab","cat"],
            [[0,1],[1,0]],
        )

    def test_3(self):
        self.run_test(
            ["a",""],
            [[0,1],[1,0]],
        )

    def test_4(self):
        self.run_test(
            ["a","b","c","ab","ac","aa"],
            [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]
        )

try:
    unittest.main()
except SystemExit:
    None

